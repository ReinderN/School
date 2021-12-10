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
