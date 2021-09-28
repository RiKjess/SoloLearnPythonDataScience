"""
The given code includes a list of heights for various basketball players.
You need to calculate and output how many players are in the range of one standard deviation from the mean.
"""

import math

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

n = 0

mean = sum(players)/len(players)

var = sum((i - mean) ** 2 for i in players)/len(players)

sd = math.sqrt(var)

x =[]

for i in players:
    if (math.fabs(mean - i) <= math.fabs(sd)):
        n += 1
        x.append(i)
print("Number of players:",n)
print("Players heights:",x)