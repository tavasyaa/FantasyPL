import pandas as pd
import json, requests, os
from pandas.io.json import json_normalize
from matplotlib import pyplot as plt

# Fantasy team stats
gwaverages = []
gwnumber = []
teamhistory = []
teamrank = []

# Player analysis
pointspergame = []
totalpoints = []
totalminutes = []
price = []


# A function to get json data from the Fantasy PL API and write it to a file. 
# We don't strictly need to write it to use it, but I'm doing that in case I want to use 
# it for other purposes/look at it in Excel. 
# data is type request. jsonResponse is type json. json.dump is a string of json.
# Remember that 'elements' are players
def get_json(file_path, type):
	# dump contents of bootstrap
	if type == 'bootstrap':
		data = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
	# dump contents of team history :)
	elif type == 'history':
		data = requests.get('https://fantasy.premierleague.com/api/entry/2612666/history/')
	# current team data
	else:
		data = requests.get('https://fantasy.premierleague.com/api/my-team/2612666/')
		
	jsonResponse = data.json()
	with open(file_path, 'w') as outfile:
		json.dump(jsonResponse, outfile)

get_json(os.path.expanduser('~/Desktop/Code/FantasyPL/FantasyPLBootstrap.json'), 'bootstrap')
get_json(os.path.expanduser('~/Desktop/Code/FantasyPL/FantasyPLTeamHistory.json'), 'history')

# json.load turns the loaded string back into type json, now we want to see normalized gameweek data:
with open(os.path.expanduser('~/Desktop/Code/FantasyPL/FantasyPLBootstrap.json')) as json_data:
	bootstrapdata = json.load(json_data)

	# Populating our arrays with data, the next thing we do is sort the data for PPG and PPM and see the top ones, then we can 
	# use Points/$ as well later
	for i in range(len(bootstrapdata['elements'])):
		pointspergame.append({bootstrapdata['elements'][i]['web_name']: bootstrapdata['elements'][i]['points_per_game']})
		totalpoints.append({bootstrapdata['elements'][i]['web_name']: bootstrapdata['elements'][i]['total_points']})
		totalminutes.append({bootstrapdata['elements'][i]['web_name']: bootstrapdata['elements'][i]['minutes']})
		totalminutes.append({bootstrapdata['elements'][i]['web_name']: bootstrapdata['elements'][i]['now_cost']})

with open(os.path.expanduser('~/Desktop/Code/FantasyPL/FantasyPLTeamHistory.json')) as json_data:
	historydata = json.load(json_data)

	# To print all the keys you can use to access data
	# print(list(data.keys()))
	# To print all gameweek information in a tabular form:
	# print(pd.json_normalize(data['events']))
	#print(data['events'][35]['average_entry_score'])

for i in range(len(historydata['current'])):
	#print(data['events'][i]['average_entry_score'])
	gwnumber.append(i+1)
	gwaverages.append(bootstrapdata['events'][i]['average_entry_score'])
	teamhistory.append(historydata['current'][i]['points'])
	teamrank.append(historydata['current'][i]['overall_rank'])

#print('Gameweek averages:',gwaverages)
#print('For gameweek numbers:',gwnumber)
#print('My team scores:', teamhistory)
#print('My overall rankings:', teamrank)
#print(list(bootstrapdata['elements'][0].keys()))
print(len(pointspergame))


# This plot shows general averages across gameweeks for players
fig = plt.figure()
axis1 = fig.add_subplot(2, 2, 1)
axis2 = fig.add_subplot(2, 2, 2)

axis1.plot(gwnumber, teamhistory, label = 'My team')
axis1.plot(gwnumber, gwaverages, label = 'Gameweek averages')
axis1.set_xlabel('Gameweek #')
axis1.set_ylabel('Points')
axis1.set_title('Fantasy PL: Points History')
axis1.legend()

axis2.plot(gwnumber, teamrank, label = 'Overall rank')
axis2.set_xlabel('Gameweek #')
axis2.set_ylabel('Overall rank #')
axis2.set_title('Fantasy PL: Rank History')
axis2.legend()

plt.show()
