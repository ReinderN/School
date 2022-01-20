#
# wk1ex2a.py
# 

import random          # importeer de module met de naam random


def rps():

    user = input("Kies je wapen [steen, papier, schaar]: ")
    comp = random.choice(['steen', 'papier', 'schaar'])

    print()
    print("User:", user)
    print("Computer:", comp)
    print()

    #De lijn hieronder controleerd of het gelijk spel is en print dan een stuk tekst met het resultaat + wat de computer en de user gekozen hebben
    if user == comp:
        print("We hebben alle twee", user, "gekozen, het is dus gelijkspel geworden.")

    #De lijnen hieronder controleren of de user zou winnen en print dan een stuk tekst met wat de computer gekozen heeft en dat de user gewonnen heeft.
    elif user == "steen" and comp == "schaar":
        print("Gefeliciteerd jij hebt gewonnen omdat ik", comp, "koos!")
    elif user == "papier" and comp == "steen":
        print("Gefeliciteerd jij hebt gewonnen omdat ik", comp, "koos!")
    elif user == "schaar" and comp == "papier":
        print("Gefeliciteerd jij hebt gewonnen omdat ik", comp, "koos!")

    #De lijnen hieronder kijken of de user verloren heeft en print dan een tekst waarin staat dat de user verloren heeft en wat de computer koos.
    elif user == "steen" and comp == "papier":
        print("Jammer je hebt verloren omdat ik", comp,"had gekozen.")
    elif user == "papier" and comp == "schaar":
        print("Jammer je hebt verloren omdat ik", comp,"had gekozen.")
    elif user == "schaar" and comp == "steen":
        print("Jammer je hebt verloren omdat ik", comp,"had gekozen.")