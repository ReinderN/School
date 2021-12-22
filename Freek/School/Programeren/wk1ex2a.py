# Naam: Freek van Witzenburg
# Bestandsnaam: wk1ex2a.py
# Opdracht: maak een variant van steen-papier-schaar 

import random          


def rps():
    """ this plays a game of Sword-Shield-pistol in Dutch ("zwaard"-"schild"-"pistool")

    """
    user = input("Kies je wapen [zwaard, schild, pistool ]: ")
    comp = random.choice(['zwaard', 'schild', 'pistool'])
    print()

    print('U koos', user)
    print('J.A.R.V.I.S.  koos', comp)
    print()

    if comp == 'Zwaard':
        print('Goed gespeeld meneer, U wint')
    if user == 'schild':
        print("Goed gespeeld J.A.R.V.i.S, ik win de volgende keer wel!")
    
