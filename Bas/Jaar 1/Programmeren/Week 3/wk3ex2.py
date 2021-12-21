# Programmeren I, week 3 opgave 2
# Bestandsnaam: wk3ex2.py
# Naam: Bas Mellens
# Probleemomschrijving: Slaapwandelende student

from random import *


def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return choice([-1, 1])

def rwpos(start, nsteps):
    """rwpos gives the position of the sleepwalker after nsteps random."""
    if nsteps < 0:
        return 0
    start = start + rs()
    rwpos(start, nsteps-1)
    print("start is: ", start)

def rwsteps(start, low, hi):
    """rwpsteps needs a starting postion and then takes a random amount of steps between low and high
    
    low: the minimum amount of steps you want the bot to take
    high: the maximum amount of steps you want the bot to take
    
    returns the amount of steps the bot has taken
    """
    if low < 0:
        return 0
    steps = randint(low, hi)
    step = rs()
    start += step
    print("|","_"*(5+step), "😴", "_"*(5-step),"|")
    steps -= 1
    return 1 + rwsteps(start, steps, steps)

def rwpos_plain(start, nsteps):
    """rwpos gets a starting position and the amount of steps the bot needs to take to get a final position
    
    start: the starting position for the bot as an int
    nsteps: the amount of steps the bot needs to take as a int

    returns the amount of steps the bot has taken
    """
    if nsteps == 0:
        return start
    start += rs()
    return rwpos_plain(start, nsteps-1)

def ave_signed_displacement(numtrials):
    lc = [rwpos_plain(0,100) for x in range(numtrials)]
    print(sum(lc)/len(lc))

def ave_squared_displacement(numtrials):
    lc = [rwpos_plain(0,100) for x in range(numtrials)]
    kwadrant = [x**2 for x in lc]
    print(sum(kwadrant)/len(kwadrant))

#resultaten ave_signed_displacement
#1. -0.2236 2. 0.1228 3. 0.0288 4. -0.2016 5. -0.1512
#Om dit te kunnen bereken heb ik 5 keer 500 recursies uitgevoerd en de resultaten daarven gemideld te nemen
#Hieruit blijkt dus dat de gemiddelde totale afwijking dus rond de 0 zit na het zetten van 100 willekeurige stappen
#Ook heb ik het geprobeerd met 500 stappen en daar kwam uit dat het nog steeds ongeveer rond de 0 zit


#resultaten ave_squared_displacement
#1. 99.4176 2. 99.264 3. 100.3752 4. 98.8264 5. 97.1792
#Om dit te kunnen bereken heb ik 5 keer 500 recursies uitgevoerd en de resultaten daarvan tot de macht 2 gedaan en het gemiddelde daar weer van te nemen
#Het gemiddelde is dus na het zetten van 100 stappen is rond de 100
#Het gemiddelde nu het zetten van 500 willekeurige stappen is nu rond de 500

#Dus het gemmidelde van ave_signed_displacement hangt af van de start en het gemidelde van ave_squared_displacement hangt af van het totaal aantal stappen