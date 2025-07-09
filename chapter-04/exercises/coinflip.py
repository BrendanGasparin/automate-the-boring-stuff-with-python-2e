# coinflip.py
# Date: Wednesday 9th July 2025
# Author: Brendan Gasparin <brendan.gasparin@gmail.com>
# Calculates the percentage chance of getting a 6-in-a-row
# coin flip streak during 100 coin flips.

import random

streaks = 0

for experimentNumber in range(10000):
    # Creates a list of 100 heads to tails values.
    flips = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')

    # Check if there is a streak of heads or tails in a row.
    count = 0
    lastside = '0'
    for i in range(len(flips)):
        if flips[i] == 'H' and lastside == 'H':
            count += 1
        elif flips[i] == 'H':
            if count > 5:
                streaks += 1
                break
            lastside == 'H'
            count = 1

        if flips[i] == 'T' and lastside == 'T':
            count += 1
        elif flips[i] == 'T':
            if count > 5:
                streaks += 1
                break
            lastside = 'T'
            count = 1

# Calculates percentage change of a six-in-a-row streak in 100 coin flips.
print('Chance of streak: %s%%' % (streaks / 100))
