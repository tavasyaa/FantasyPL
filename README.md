# FantasyPL

### Python, using Matplotlib, Pandas, the Fantasy Premier League API, and the Understat API

I'm an avid fan of the English Premier League, and every year I play Fantasy Premier League with my friends, who all put in a set amount of money in a pot for the winner to grab.

Hopefully this ups my chances of winning some money from my friends : )

1. First, I analyze my team's performance by comparing points/gameweek to the FPL average. 
2. I delve into players' points(P), points/minute(P/M), points/game(P/G), points/$(P/$), and minutes(Min) values to see if I can uncover any hidden gems. Here, we look at the top players in each dimension; we also include a floor of minutes played for P/M.
3. I look at xG, xA and expected FPL points from Understat data, and try to discern who overperforming(-PD) and underperforming(+PD) players are based on an expected points model(EP) (Ustat.py)
4. Let's make a team! I experiment using my intuition and a pretty simple algorithm.

#### Assumptions: 

We'll play a 4-3-3, and we'll adhere to FPL's max-3-players-from-a-club rule. We'll pick the cheapest bench possible -- as of today (04/09/2020), that's Norris (GK @ 3.9), Kilman (DEF @ 3.9), Guendouzi (MID @ 4.2), Elneny (MID @ 4.2), and Connolly (ST @ 4.2). This leaves us with 79.6 to spend on our starting 11. We also won't take into account upcoming fixtures, relationship with the manager, recent injuries, and other miscellaneous factors to keep your eye on. I use two methods: in the first, I simply look through the lists to see who top players are. In the second, I implement an algorithm that picks as many players with max points as it can, followed by players with the best points/$. The algorithm can be tweaked to also pick an entire FPL squad with subs too -- something that could be useful!

###### The Eyeball Method

GK: Pope(P/$)\
DEF: Soyuncu(P/$), Alonso(P/G), Baldock(P/$), Lundstram(P/$)\
MID: Salah(P), De Bruyne(P), Cantwell(P/$)\
ST:  Jota(+PD), Vardy(-PD), Jimenez(EP)

###### The Algorithm Method

GK: Pope\
DEF: Van Dijk, Lundstram, Baldock, Stevens\
MID: Salah, De Bruyne, Mane\
ST:  Ayew, Ings, Greenwood

#### More ideas, maybe in the future: 

- Quantify form: P/$ in last 5 games
- Let the algorithm pick a formation
- Build a score based on weights of each dimension, and then build an algorithm to pick players based on the score
- A more complex, predictive version of building a team

#### Acknowledgements:

Thanks to official FPL, who make their REST API open to the public. Thanks also to Amos Bastian and his API for Understat soccer data, which can be found [here](https://github.com/amosbastian/understat).