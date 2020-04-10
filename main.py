import pandas as pd
import json, requests, os
from pandas.io.json import json_normalize
from matplotlib import pyplot as plt

# SECTION 1: Fantasy team stats

gwaverages = []
gwnumber = []
teamhistory = []
teamrank = []

# A function to get json data from the Fantasy PL API and write it to a file. We don't strictly need to write 
#it to use it, but I'm doing that in case I want to use it for other purposes/look at it in Excel. 
# data is type request. jsonResponse is type json. json.dump is a string of json. 'elements' are players
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

#SECTION 2: Player analysis

playerdata = bootstrapdata['elements']

for i in range(len(playerdata)):
	playerdata[i]['points_per_dollar'] = playerdata[i]['total_points'] / playerdata[i]['now_cost'] / 10

	if playerdata[i]['minutes'] != 0:
		playerdata[i]['points_per_minute'] = playerdata[i]['total_points'] / playerdata[i]['minutes']
	else:
		playerdata[i]['points_per_minute'] = 0

# Sorts by a certain key in the dictionary
sortedpoints = sorted(playerdata, key=lambda k: k['total_points'], reverse = True) 
sortedminutes = sorted(playerdata, key=lambda k: k['minutes'], reverse = True) 
sortedppg = sorted(playerdata, key=lambda k: k['points_per_game'], reverse = True)
sortedppd = sorted(playerdata, key=lambda k: k['points_per_dollar'], reverse = True)
sortedppm = sorted(playerdata, key=lambda k: k['points_per_minute'], reverse = True)

print('TOP 20 PLAYERS ON THE FOLLOWING DIMENSIONS ARE:')

# Points per minute are useful to identify bench players, or players who you know will play more in the future
print('PPM: PPM: PPM: PPM: PPM: PPM: PPM: PPM: PPM: PPM: ')
counter = 0
for i in range(len(playerdata)):
	if (sortedppm[i]['minutes']) > 500:
		print(sortedppm[i]['web_name'], sortedppm[i]['points_per_minute'])
		counter = counter + 1
	if counter == 20:
		break

# To identify Mr. Reliables, they'll always play
print('MINUTES: MINUTES: MINUTES: MINUTES: MINUTES: ')
for i in range(20):
	print(sortedminutes[i]['web_name'], sortedminutes[i]['minutes'])

# Self-explanatory, it will be too expensive to feature a lot of them at once
print('POINTS: POINTS: POINTS: POINTS: POINTS: POINTS: ')
for i in range(20):
	print(sortedpoints[i]['web_name'], sortedpoints[i]['total_points'])

# Bang for your buck -- a key insight not provided by FPL
print('PP$: PP$: PP$: PP$: PP$: PP$: PP$: PP$: PP$: ')
for i in range(20):
	print(sortedppd[i]['web_name'], sortedppd[i]['points_per_dollar'])

# Points per game -- if they are returning from injury, a high PPG could mean they are a future great pick
print('PPG: PPG: PPG: PPG: PPG: PPG: PPG: PPG: PPG: ')
for i in range(20):
	print(sortedppg[i]['web_name'], sortedppg[i]['points_per_game'])


# SECTION 4: Building a team with the ranked data
# then, you can go down the ppm or ppd or ppg array and see what team you can afford - and which gets the highest points tally
# Restructure code? Set up excels etc in one file, do section 1 in one, and section 2 in the other possibly

#A great idea is to look at expected points - points to find undervalued players: here eP would be 
# xG * points for a goal + xA * points for an assist etc




