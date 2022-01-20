#
# wk9ex2.py
#
# Namen: Reinder Noordmans, Bas Mellens & Freek van Witzenburg
#


# dit is een functie om tweedimensionale arrays
#  (lijsten van lijsten) af te drukken
def print_2d(a):
    """print_2d prints a 2D array, a
       as rows and columns
       Argument: a, a 2D list of lists
       Result: None (no return value)
    """
    rows = len(a)
    cols = len(a[0])

    for r in range(rows):      # rows == aantal rijen
        for c in range(cols):  # cols == aantal kolommen
            print(a[r][c], end=' ')
        print()
    # als er geen return-statement aanwezig is


# een paar tests voor print_2d
a = [['X', ' ', 'O'], ['O', 'X', 'O']]
print("2-row, 3-col a is")
print_2d(a)

a = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
print("4-row, 2-col a is")
print_2d(a)


# maak een tweedimensionale array van een ééndimensionale string
def create_a(rows, cols, s):
    """Returns a 2D array with
       rows rows and
       cols cols
       using the data from s: across the
       first row, then the second, etc.
       We'll only test it with enough data!
    """
    a = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row += [s[0]]  # voeg dat karakter toe
            s = s[1:]          # verwijder het eerste karakter
        a += [new_row]
    return a


# een paar tests voor create_a:
a = [['X', ' ', 'O'], ['O', 'X', 'O']]
new_a = create_a(2, 3, 'X OOXO')
assert new_a == a
print("Is new_a == a? moet True zijn:", new_a == a)

a = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
new_a = create_a(4, 2, 'XO XOOOX')
assert new_a == a


def in_a_row_3_east(ch, r_start, c_start, a):
    '''this function tests if the board has 3 in a row somewhere to the east from a starting position.'''
    # voor de functie voor drie op een rij naar het oosten:

    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])   # aantal kolommen is len(a[0])

    if r_start > rows:
        return False  # buiten de grenzen van de rijen

    # andere grenscontroles...
    if c_start > cols - 3:
        return False  # buiten de grenzen van de kolommen

    # zijn alle gegevenselementen correct?
    for i in range(3):                   # lusindex is i
        if a[r_start][c_start+i] != ch:  # controleer op fouten
            return False                 # fout gevonden; geef False terug

    return True                          # geen fouten gevonden in de lus; geef True terug


def in_a_row_3_south(ch, r_start, c_start, a):
    '''this function tests if the board has 3 in a row somewhere to the south from a starting position.'''
    # voor de functie voor drie op een rij naar het oosten:

    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])   # aantal kolommen is len(a[0])

    if r_start > rows-3:
        return False  # buiten de grenzen van de rijen

    # andere grenscontroles...
    if c_start > cols:
        return False  # buiten de grenzen van de kolommen

    # zijn alle gegevenselementen correct?
    for i in range(3):                   # lusindex is i
        if a[r_start+i][c_start] != ch:  # controleer op fouten
            return False                 # fout gevonden; geef False terug

    return True                          # geen fouten gevonden in de lus; geef True terug


def in_a_row_3_southeast(ch, r_start, c_start, a):
    '''this function tests if the board has 3 in a row somewhere to the southeast from a starting position.'''
    # voor de functie voor drie op een rij naar het oosten:

    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])   # aantal kolommen is len(a[0])

    if r_start > rows-3:
        return False  # buiten de grenzen van de rijen

    # andere grenscontroles...
    if c_start > cols - 3:
        return False  # buiten de grenzen van de kolommen

    # zijn alle gegevenselementen correct?
    for i in range(3):                   # lusindex is i
        if a[r_start+i][c_start+i] != ch:  # controleer op fouten
            return False                 # fout gevonden; geef False terug

    return True                          # geen fouten gevonden in de lus; geef True terug


def in_a_row_3_northeast(ch, r_start, c_start, a):
    '''this function tests if the board has 3 in a row somewhere to the northeast from a starting position.'''
    # voor de functie voor drie op een rij naar het oosten:

    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])   # aantal kolommen is len(a[0])

    if r_start > rows:
        return False  # buiten de grenzen van de rijen

    # andere grenscontroles...
    if c_start > cols - 3:
        return False  # buiten de grenzen van de kolommen

    # zijn alle gegevenselementen correct?
    for i in range(3):                   # lusindex is i
        if a[r_start-i][c_start+i] != ch:  # controleer op fouten
            return False                 # fout gevonden; geef False terug

    return True                          # geen fouten gevonden in de lus; geef True terug


def in_a_row_n_east(ch, r_start, c_start, a, n):
    '''this function tests if the board has n in a row somewhere to the east from a starting position.'''
    # voor de functie voor drie op een rij naar het oosten:

    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])   # aantal kolommen is len(a[0])

    if r_start > rows:
        return False  # buiten de grenzen van de rijen

    # andere grenscontroles...
    if c_start > cols - n:
        return False  # buiten de grenzen van de kolommen

    # zijn alle gegevenselementen correct?
    for i in range(n):                   # lusindex is i
        if a[r_start][c_start+i] != ch:  # controleer op fouten
            return False                 # fout gevonden; geef False terug

    return True                          # geen fouten gevonden in de lus; geef True terug


def in_a_row_n_south(ch, r_start, c_start, a, n):
    '''this function tests if the board has n in a row somewhere to the south from a starting position.'''
    # voor de functie voor drie op een rij naar het oosten:

    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])   # aantal kolommen is len(a[0])

    if r_start > rows - n:
        return False  # buiten de grenzen van de rijen

    # andere grenscontroles...
    if c_start > cols:
        return False  # buiten de grenzen van de kolommen

    # zijn alle gegevenselementen correct?
    for i in range(n):                   # lusindex is i
        if a[r_start+i][c_start] != ch:  # controleer op fouten
            return False                 # fout gevonden; geef False terug

    return True                          # geen fouten gevonden in de lus; geef True terug


def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    '''this function tests if the board has n in a row somewhere to the southeast from a starting position.'''
    # voor de functie voor drie op een rij naar het oosten:

    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])   # aantal kolommen is len(a[0])

    if r_start > rows - n:
        return False  # buiten de grenzen van de rijen

    # andere grenscontroles...
    if c_start > cols - n:
        return False  # buiten de grenzen van de kolommen

    # zijn alle gegevenselementen correct?
    for i in range(n):                   # lusindex is i
        if a[r_start+i][c_start+i] != ch:  # controleer op fouten
            return False                 # fout gevonden; geef False terug

    return True                          # geen fouten gevonden in de lus; geef True terug


def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    '''this function tests if the board has n in a row somewhere to the northeast from a starting position.'''
    # voor de functie voor drie op een rij naar het oosten:

    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])   # aantal kolommen is len(a[0])

    if r_start > rows:
        return False  # buiten de grenzen van de rijen

    # andere grenscontroles...
    if c_start > cols - n:
        return False  # buiten de grenzen van de kolommen

    # zijn alle gegevenselementen correct?
    for i in range(n):                   # lusindex is i
        if a[r_start-i][c_start+i] != ch:  # controleer op fouten
            return False                 # fout gevonden; geef False terug

    return True                          # geen fouten gevonden in de lus; geef True terug


a = create_a(4, 4, 'XXOXOOXXOOXXXXXO')
assert in_a_row_3_east('X', 3, 0, a)
assert not in_a_row_3_east('O', 1, 0, a)

assert in_a_row_3_south('X', 1, 2, a)
assert not in_a_row_3_south('O', 1, 0, a)

assert in_a_row_3_southeast('X', 0, 1, a)
assert not in_a_row_3_southeast('X', 2, 3, a)

assert in_a_row_3_northeast('X', 3, 1, a)
assert not in_a_row_3_northeast('O', 3, 3, a)

a = create_a(5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
assert in_a_row_n_east('X', 0, 0, a, 2)
assert not in_a_row_n_east('X', 0, 0, a, 3)

assert in_a_row_n_south('X', 0, 1, a, 1)
assert not in_a_row_n_south('O', 4, 4, a, 4)

assert in_a_row_n_southeast('X', 2, 2, a, 2)
assert not in_a_row_n_southeast('O', 2, 0, a, 4)

assert in_a_row_n_northeast('X', 4, 3, a, 2)
assert not in_a_row_n_northeast('O', 1, 3, a, 3)
