#
# wk1ex2a.py
#

import random          


def rps():

    user = input("Kies steen, papier of schaar: ")
    comp = random.choice(['steen', 'papier', 'schaar'])
    print()

    print('Jij koos', user)
    print('Ik  koos', comp)
    print()

    if user == comp:
        print('Gelijkspel verdomme')
    elif user == 'steen':
        if comp == 'papier':
            print('Haha gewonnen!')
        elif comp == 'schaar':
            print('Jij wint (sadface)')
    elif user == 'papier':
        if comp == 'schaar':
            print('Jij wint (sadface)')
        elif comp == 'steen':
            print('Haha ik win!')
    elif user == 'schaar':
        if comp == 'papier':
            print('Jij wint (sadface)')
        elif comp == 'steen':
            print('Loser ik win!!')
    else:
        print('Foute keuze kies iets anders.')

    print()        