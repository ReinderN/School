# Programmeren I, week 3 opgave 2
# Bestandsnaam: wk3ex2.py
# Naam: Reinder Noordmans
# Probleemomschrijving: Slaapwandelende student

from random import *


def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return choice([-1, 1])

def rwpos(start, nsteps):
    """rwpos gets a starting position and the amount of steps the bot needs to take to get a final position
    
    start: the starting position for the bot as an int
    nsteps: the amount of steps the bot needs to take as a int

    returns the amount of steps the bot has taken
    """
    print(start)
    if nsteps == 0:
        return 0
    else:
        start += rs()
        return 1 + rwpos(start, nsteps-1)

def rwsteps(start, low, hi):
    """rwpsteps needs a starting postion and then takes a random amount of steps between low and high
    
    low: the minimum amount of steps you want the bot to take
    high: the maximum amount of steps you want the bot to take
    
    returns the amount of steps the bot has taken
    """
    if low < 0:
        return 0
    else:
        steps = randint(low, hi)
        step = rs()
        start += step
        print("|","_"*(5+step), "😴", "_"*(5-step),"|")
        steps -= 1
        return 1 + rwsteps(start, steps, steps)

