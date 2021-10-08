# Programmeren I, week 3 opgave 2
# Bestandsnaam: wk3ex2.py
# Naam:
# Probleemomschrijving: Slaapwandelende student

import random  


def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
   