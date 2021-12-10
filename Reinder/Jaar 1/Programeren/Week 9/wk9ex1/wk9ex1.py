#
# wk9ex1.py - Practicum Game of Life
#
# Naam:
#

import random


def create_one_row(width):
    """ returns one row of zeros of width "width"...  
        You might use this in your create_board(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row


def create_board(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    a = []
    for row in range(height):
        # gebruik de bovenstaande functie zodat ... één rij is!!
        a += [create_one_row(width)]
    return a


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


def inner_cells(width, height):

    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            a[row][col] = 1
    return a


def random_cells(width, height):

    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            a[row][col] = random.choice([0, 1])
    return a
