def next(term):
    '''
    Deze functie berekent het volgende nummer in de rij van Conway

    term: Int
    returns: Int
    '''

    output = ''  # Initialiseerd de output
    count = 0  # Initialiseerd de count

    # Verandert de term naar een string zodat het verwerkt kan worden in een for loop
    term = str(term)
    # Dit is de totale lengte van de term
    lent = len(term)

    # enumerate word hierbij gebruikt om ook een index waarde te geven
    for i, x in enumerate(term):
        count += 1  # Telt 1 punt bij de count op omdat er weer 1 item is

        # Controleerd of de huidige index positie het laatste cijfer is in de string
        if i == lent-1:
            # Geeft bij de output het aantal items en welk item dat is
            # Daarna word de count gereset omdat er een nieuw nummer aan kan komen (niet hier want dit is het einde maar toch handig)
            output += str(count) + str(x)
            count = 0

        # Controleerd of de huidige x hetzelfde is als de volgende x
        elif x == term[i+1]:
            # Doet niks aan de telling omdat er weer een item komt met dezelfde waarde
            count += 0

        # Als niks van hierboven waar is word dit uitgevoerd
        else:
            # Geeft bij de output het aantal items en welk item dat is
            # Daarna word de count gereset omdat er een nieuw nummer aan kan komen
            output += str(count) + str(x)
            count = 0

    # Geeft het volgende item in de rij terug
    return int(output)


# Assert statements next(term):
assert next(22) == 22
assert next(1) == 11
assert next(312211) == 13112221
assert next(11) == 21
assert next(1211) == 111221


def read_it(n):
    '''
    Deze functie gaat telt vanaf 1 door n aantal Conway nummers in de rij van Conway

    n: Int
    output: None
    '''
    current = 1  # begint altijd bij 1
    for x in range(n):  # gaat door alles in n heen
        print(current)  # print het huidige cijfer
        current = next(current)  # berekent het volgende cijfer


# print test voor read_it
read_it(6)
