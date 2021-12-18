# namen: Reinder Noordmans, Bas Mellens, Freek van Witzenburg

def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Voer een nieuwe lijst in")
    print("(1) Druk de huidige lijst af")
    print("(2) Bepaal de gemiddelde prijs")
    print("(3) Bepaal de standaardafwijking")
    print("(4) Bepaal het minimum en de bijbehorende dag")
    print("(5) Bepaal het maximum en de bijbehorende dag")
    print("(6) Je TR-investeringsplan")
    print("(9) Stoppen")
    print()


def new_list(new_L):
    '''deze functie zet een string om in een lijst'''
    try:
        # eval voert de Python-interpreter uit! Let op: Gevaarlijk!
        new_L = eval(new_L)
        if not isinstance(new_L, list):
            print("Dat lijkt geen lijst. L wordt niet aangepast.")
        else:
            L = new_L  # Hier is het wel OK, dus we passen onze lijst L aan
    except:
        print("Ik begreep de invoer niet. L wordt niet aangepast.")
    return L


def standaardafwijking(ls):
    '''Deze functie berekent de standaard afwijking in een lijst '''
    som = 0
    ok = 0
    n = len(ls)
    for x in ls:
        som += x
    mean = som / n
    for x in ls:
        ok += (x - mean)**2
    var = ok/n
    std_dev = var ** 0.5
    return std_dev


def maxcalc(L):
    '''deze functie berekent het maximum bedrag in een lijst en geeft de dag ook mee'''
    max = [0, 0]
    for i, x in enumerate(L):
        if x > max[0]:
            max = [x, i]
    return max


def mincalc(L):
    '''deze functie berekent het minimum bedrag in een lijst en geeft de dag ook mee'''
    min = [99999999999, 0]
    for i, x in enumerate(L):
        if x < min[0]:
            min = [x, i]
    return min


def main():
    '''deze functie is het hart van het programa'''
    while True:
        menu()
        choice = input("Maak een keuze: ")
        try:
            choice = int(choice)   # omzetten naar een int!
        except:
            print("Ik begreep de invoer niet! Verder gaan...")
            continue
        if choice == 9:
            break
        elif choice == 0:
            new_L = input('Nieuwe lijst: ')
            L = new_list(new_L)
        elif choice == 1:
            print('Dag  Prijs')
            print('---  -----')
            for dag, prijs in enumerate(L):
                print(dag, '  ', prijs)
        elif choice == 2:
            lL = len(L)
            som = 0
            for x in L:
                som += x
            gem = som/lL
            print(gem)
        elif choice == 3:
            stdafwk = standaardafwijking(L)
            print(stdafwk)
        elif choice == 4:
            min = mincalc(L)
            print('Laagste prijs was €', min[0], 'op dag', min[1])
        elif choice == 5:
            max = maxcalc(L)
            print('Laagste prijs was €', max[0], 'op dag', max[1])
        elif choice == 6:
            minadv = mincalc(L)
            maxadv = maxcalc(L)
            print('Je TRI investeringsstrategie is om')
            print()
            print('Te kopen op dag', minadv[1], 'voor prijs €', minadv[0])
            print('Te verkopen op dag', maxadv[1], 'voor prijs €', maxadv[0])
            print()
            print('Je totale winst is dan: €', maxadv[0]-minadv[0])


assert new_list('[10,20,30,40,50]') == [10, 20, 30, 40, 50]
assert new_list('[10,30,40,59]') == [10, 30, 40, 59]

assert maxcalc([10, 20, 30, 40, 50]) == [50, 4]
assert mincalc([10, 20, 30, 40, 50]) == [10, 0]
