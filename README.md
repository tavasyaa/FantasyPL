# FantasyPL

### Python, using Matplotlib and Pandas

I'm an avid fan of the English Premier League, and every year I play Fantasy Premier League with my friends, who all put in a set amount of money in a pot for the winner to grab.

Hopefully this ups my chances of winning some money from my friends :)

1. First, I analyze my team's performance by comparing points/gameweek to the FPL average. 
2. I delve into players' points(P), points/minute(P/M), points/game(P/G), points/$(P/$), and minutes(Min) values to see if I can uncover any hidden gems. Here, we look at the top players in each dimension; we also include a floor of minutes played for P/M.
3. I look at xG, xA and expected FPL points from Understat data, and try to discern who overperforming(-PD) and underperforming(+PD) players are based on an expected points model(EP) (Ustat.py)
4. Let's make a team! Coming soon (may do it programmatically soon too), ways to use this data to create a high-performing FPL team!

#### Assumptions: 
We'll play a 4-3-3, and we'll pick the cheapest bench possible. As of today (04/09/2020), that's Norris (GK @ 3.9), Kilman (DEF @ 3.9), Guendouzi (MID @ 4.2), Elneny (MID @ 4.2), and Connolly (ST @ 4.2). This leaves us with 79.6 to spend on our starting 11. We also won't take into account upcoming fixtures, relationship with the manager, recent injuries, and other miscellaneous factors to keep your eye on.

###### The Eyeball Method

GK: Pope(P/$)\
DEF: Soyuncu(P/$), Alonso(P/G), Baldock(P/$), Lundstram(P/$)\
MID: Salah(P), De Bruyne(P), Henderson(P/$)\
ST:  Jota(+PD), Vardy(-PD), Jimenez(EP)

###### The Algorithm Method


#### Appendix (lists I refer to here):

Finally, I'd like to add that I'm not necessarily an advocate of using just numbers to build a team -- the eye test can be particularly useful too!

#### More ideas, maybe in the future: 
- Quantify form: P/$ in last 5 games


#### Acknowledgements: