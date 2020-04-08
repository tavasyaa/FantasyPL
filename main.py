import pandas as pd
import json, requests, os
from pandas.io.json import json_normalize
from matplotlib import pyplot as plt

### SECTION 1: My team vs FPL averages

gwaverages = []
gwnumber = []
teamhistory = []

# A function to get json data from the Fantasy PL API and write it to a file. 
# We don't strictly need to write it to use it, but I'm doing that in case I want to use it for other purposes/look at it in Excel. 
# data is type request. jsonResponse is type json. json.dump is a string of json.
# Remember that 'elements' are players
def get_json(file_path, type):
	# dump contents of bootstrap
	if type == 'bootstrap':
		data = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
		jsonResponse = data.json()
		with open(file_path, 'w') as outfile:
			json.dump(jsonResponse, outfile)
	# dump contents of team history :)
	else:
		data = requests.get('https://fantasy.premierleague.com/api/entry/2612666/history/')
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

print('Gameweek averages:',gwaverages)
print('For gameweek numbers:',gwnumber)
print('My team scores:', teamhistory)

# This plot shows general averages across gameweeks for players
plt.plot(gwnumber, teamhistory, label = 'My team')
plt.plot(gwnumber, gwaverages, label = 'Gameweek averages')
plt.xlabel('Gameweek #')
plt.ylabel('Points')
plt.title('Fantasy PL: 2019-20')
plt.legend()
plt.show()





