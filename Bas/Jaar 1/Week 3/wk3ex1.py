#
# wk3ex1.py
#
# Naam: Bas Mellens
#
# Turtle graphics en recursie
#

import time
from turtle import *
from random import *


def tri(n):
    """Draws n 100-pixel sides of an equilateral triangle.
       Note that n doesn't have to be 3 (!)
    """
    width(1)
    clr = (0, 0.8, 0.2)
    color(clr)
    shape('turtle')
    if n == 0:
        return
    else:
        dot(10, 'red')
        forward(100)
        left(120)
        tri(n-1)

def spiral(initial_length, angle, multiplier):
    """Spiral-drawing function.  Arguments:
       initial_length = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
    shape('turtle')
    if initial_length <= 1:          
        return
    else:
        forward(initial_length)
        left(angle)
        initial_length *= multiplier
        spiral(initial_length, angle, multiplier)
        