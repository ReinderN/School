#
# wk9ex1.py - Practicum Game of Life
#
# Naam: BL.P.R. Noordmans, B. Mellens, F.M. van Witzenburg
#

import random


def create_one_row(width):
    """ returns one row of zeros of width "width"...
        You might use this in your create_board(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row


assert create_one_row(5) == [0, 0, 0, 0, 0]
assert create_one_row(2) == [0, 0]
assert create_one_row(7) == [0, 0, 0, 0, 0, 0, 0]


def create_board(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    a = []
    for row in range(height):
        # gebruik de bovenstaande functie zodat ... één rij is!!
        a += [create_one_row(width)]
    return a


assert create_board(5, 5) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
assert create_board(7, 4) == [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
assert create_board(8, 8) == [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


def print_board(a):
    """This function prints the 2D list-of-lists a."""
    for row in a:
        print('')               # row is de hele rij
        for col in row:         # col is het individuele element
            print(col, end='')  # druk dat element af


def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But do that only in the *interior* of the 2D array.
    """
    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                a[row][col] = 1
            else:
                a[row][col] = 0

    return a


assert diagonalize(5, 5) == [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [
    0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]
assert diagonalize(7, 4) == [[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [
    0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
assert diagonalize(8, 8) == [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [
    0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


def inner_cells(width, height):
    """ Deze functie geeft de totale levende cellen weer die zich in de tweedimensionale array bevinden."""
    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            a[row][col] = 1
    return a


assert inner_cells(5, 5) == [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [
    0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
assert inner_cells(7, 4) == [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [
    0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]]
assert inner_cells(8, 8) == [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [
    0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


def random_cells(width, height):
    """ Deze functie geeft het aantal random cellen weer dei 1 en 0 terug geeft."""
    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            a[row][col] = random.choice([0, 1])
    return a


def copy(a):
    """Returns a DEEP copy of the 2D array a."""
    height = len(a)
    width = len(a[0])
    new_a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            new_a[row][col] = a[row][col]
    return new_a


assert copy([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [
    0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]) == [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [
        0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
assert copy([[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [
    0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]) == [[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [
        0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
assert copy([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


def inner_reverse(a):
    """ Deze functie geeft zorgt ervoor dat de buitenste randen geven aan de buitenkant 
    van de array altijd 0 terug geven. """
    height = len(a)
    width = len(a[0])
    reverse_a = create_board(width, height)
    reversed_sa = 0

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if a[row][col] == 0:
                reversed_sa = 1
            else:
                reversed_sa = 0
            reverse_a[row][col] = reversed_sa
    return reverse_a


assert inner_reverse([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [
    0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
assert inner_reverse([[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [
    0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]) == [[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [
        0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]]
assert inner_reverse([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [
        0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


def count_neighbours(row, col, a):
    """ Deze functie telt alle levende buren die van een cel aanwezig zijn. """
    living_neighbours = 0

    for nrow in range(-1, 2):
        for ncol in range(-1, 2):
            if nrow == 0 and ncol == 0:
                living_neighbours += 0
            else:
                if a[row + nrow][col + ncol] == 1:
                    living_neighbours += 1
    return living_neighbours


assert count_neighbours(1, 2, [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [
    0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]) == 5
assert count_neighbours(2, 4, [[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [
    0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]) == 0
assert count_neighbours(3, 5, [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]) == 0


def next_life_generation(a):
    """Makes a copy of a and then advances one
       generation of Conway's Game of Life within
       the * inner cells * of that copy.
       The outer edge always stays at 0.
    """
    new_a = copy(a)
    height = len(a)
    width = len(a[0])

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            decision = count_neighbours(row, col, a)
            if decision < 2 or decision > 3:
                new_a[row][col] = 0
            elif decision == 3:
                new_a[row][col] = 1
            else:
                new_a[row][col] = a[row][col]
    return new_a


assert next_life_generation([[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [
    0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
