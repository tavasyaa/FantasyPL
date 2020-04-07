import pandas as pd
import json
import requests
import os
from pandas.io.json import json_normalize

# A function to get json data from the Fantasy PL API and write it to a file. data is type request. jsonResponse is type json. json.dump is a string of json.
def get_json(file_path):
	data = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
	jsonResponse = data.json()
	with open(file_path, 'w') as outfile:
		json.dump(jsonResponse, outfile)

# Calling our function
get_json(os.path.expanduser('~/Desktop/Code/FantasyPL/FantasyPL.json'))

# json.load turns the loaded string back into type json
with open(os.path.expanduser('~/Desktop/Code/FantasyPL/FantasyPL.json')) as json_data:
	data = json.load(json_data)
	print(list(data.keys()))
	print(pd.json_normalize(data['teams']))
	#print(data['teams'])