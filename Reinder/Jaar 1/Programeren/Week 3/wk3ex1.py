#
# wk3ex1.py
#
# Naam: Reinder Noordmans
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
    width(2 * n + 1)
    clr = choice(['darkgreen', 'red', 'blue'])
    color(clr)
    shape('turtle')
    if n == 0:
        reset()
        return      # Geen zijden om te tekenen, dus stop met tekenen
    dot(10, 'black')
    forward(100)
    left(120)
    tri(n-1)    # Gebruik recursie om de overige zijden te tekenen!

def spiral(initial_length, angle, multiplier):
    """Spiral-drawing function.  Arguments:
       initial_length = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
    forward(initial_length)
    if initial_length <= 1:          
        return      # Niets meer te tekenen, dus beëindig deze aanroep naar spiral
    left(angle)
    initial_length *= multiplier
    forward(initial_length)
    spiral(initial_length, angle, multiplier)

def chai(size):
    """Our chai function!"""
    if size < 5: 
        return
    forward(size)
    left(90)
    forward(size/2)
    right(90)
    chai(size / 2)
    right(90)
    forward(size)
    left(90)
    chai(size / 2)
    left(90)
    forward(size/2.0)
    right(90)
    backward(size)
    return

def svtree(trunklength, levels):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    forward(trunklength)
    left(30)
    svtree(trunklength/2,levels-1)
    right(60)
    svtree(trunklength/2,levels-1)
    left(30)
    backward(trunklength)

def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
       sidelength: pixels in the largest-scale triangle side
       levels: the number of recursive levels in each side
    """
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)

def flakeside(sidelength, levels):
    """flakeside is part of the function snowflake to make a third of its side

    sidelength: the total lenght of one side
    levels: the amount of times you want it to make spikes
    """
    if levels == 0:
        forward(sidelength)
    else:
        flakeside(sidelength/3, levels-1)
        right(60)
        flakeside(sidelength/3, levels-1)
        left(120)
        flakeside(sidelength/3, levels-1)
        right(60)
        flakeside(sidelength/3, levels-1)

def reset():
    resetscreen()
