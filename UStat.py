# SECTION 3: Calculating expected points, we'll subtract actual points soon

import asyncio
import json
import aiohttp
from understat import Understat

async def main():
	async with aiohttp.ClientSession() as session:
		understat = Understat(session)
		players = await understat.get_league_players(
			"epl",
			2019)        

		# Right now we're using a makeshift model of 4* goal and 3* assists to score, which is the 
		#norm for strikers in FPL
		for i in range(len(players)):
			players[i]['expected_points'] = 4 * float(players[i]['xG']) + 3 * float(players[i]['xA'])
			players[i]['actual_points'] = 4 * float(players[i]['goals']) + 3 * float(players[i]['assists'])
			# if points differential is positive, they are underperforming. If it is negative, overperforming. 
			# What that means is up to you! In the next couple lines, we'll rank the top 30 in both dimensions
			players[i]['points_differential'] = players[i]['expected_points'] - players[i]['actual_points']

		sortedexpectedpoints = sorted(players, key=lambda k: k['expected_points'], reverse = True)
		positivedifferentials = sorted(players, key=lambda k: k['points_differential'], reverse = True) 
		negativedifferentials = sorted(players, key=lambda k: k['points_differential']) 

		print('Expected Points Expected Points Expected Points:')
		for i in range(20):
			print(sortedexpectedpoints[i]['player_name'], sortedexpectedpoints[i]['expected_points'])

		print('Positive Points differential Positive Points differential: (underperform compared to expected)')
		for i in range(20):
			print(positivedifferentials[i]['player_name'], positivedifferentials[i]['points_differential'])

		print('Negative points differential Negative points differential: (overperform compared to expected)')
		for i in range(20):
			print(negativedifferentials[i]['player_name'], negativedifferentials[i]['points_differential'])

# Do expected points for each position later, it'll be slightly more complex

loop = asyncio.get_event_loop()
loop.run_until_complete(main())