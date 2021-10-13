# Programmeren I, Week 3 Opgave 3
# Bestandsnaam: wk3ex3.py
# Naam: Bas Mellens
# Probleemomschrijving: List comprehensions



# hiermee krijgen we functies als sin en cos...
from math import *


# twee extra functies (die niet in de module math hierboven zitten)


def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2 * x


def sq(x):
    """Squarer!  argument: x, a number"""
    return x ** 2


# voorbeelden om aan list comprehensions te wennen...


def lc_mult(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each multiplied by 2**
    """
    return [2 * x for x in range(n)]


def lc_idiv(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [float(x // 2) for x in range(n)]


def lc_fdiv(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x / 2 for x in range(n)]


assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0.0, 0.0, 1.0, 1.0]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]


# Hier begin je met de functies voor deze opgave:


# Stap 1, deel 1
def unitfracs(n):
    """unitfracs returns a list with values that are equal to 1/n ... n/n
    n: the value you want to have fractures from
    """
    return [x / n for x in range(n)]    

def scaledfracs(low, hi, n):
    """Scaledfracs returns a list of values with a fracture of the values between low and high
    low: The lower limit of the values in the list
    high: The upper limit of the values in the list
    n: the amount of times you want in between low and high
    """
    return [low + (hi-low) * x for x in unitfracs(n)]

def sqfracs(low, hi, n):
    """sqfracs returns a list with values between low and high put to the power of two
    low: The lower limit of the values in the list
    high: The upper limit of the values in the list
    n: the amount of times you want in between low and high    
    """
    return [x**2 for x in scaledfracs(low, hi, n)]

def f_of_fracs(f, low, hi, n):
    """f_of_fracs return a list of values between low and high that have been put trough another function
    f: another function
    low: The lower limit of the values in the list
    high: The upper limit of the values in the list
    n: the amount of times you want in between low and high
    """
    return [f(x) for x in scaledfracs(low, hi, n)]

def integrate(f, low, hi, n):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit hi (the third argument)
       where n steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of n uniform steps
       from low to hi
    """
    y = f_of_fracs(f, low, hi, n)
    return 2.5*sum(y)

def c(x):
    """c is a semicircular function of radius 2"""
    return (4 - x ** 2) ** 0.5

#Test de unitfracs funcite
assert unitfracs(2) == [0.0, 0.5]
assert unitfracs(5) == [0.0, 0.2, 0.4, 0.6, 0.8]
assert unitfracs(10) == [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
#Test de scaledfracs functie
assert scaledfracs(10, 30, 5) == [10.0, 14.0, 18.0, 22.0, 26.0]
assert scaledfracs(41, 43, 8) == [41.0, 41.25, 41.5, 41.75, 42.0, 42.25, 42.5, 42.75]
assert scaledfracs(0, 10, 4) == [0.0, 2.5, 5.0, 7.5]
#Test de sqfracs functie
assert sqfracs(4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert sqfracs(0, 10, 5) == [0.0, 4.0, 16.0, 36.0, 64.0]
assert sqfracs(0,100,8) == [0.0, 156.25, 625.0, 1406.25, 2500.0, 3906.25, 5625.0, 7656.25]
#Test de f_of_fracs functie
assert f_of_fracs(dbl, 10, 20, 5) == [20.0, 24.0, 28.0, 32.0, 36.0]
assert f_of_fracs(sq, 4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert f_of_fracs(sin, 0, pi, 2) == [0.0, 1.0]
#Test de integrate functie
assert integrate(dbl, 0, 10, 4) == 75
assert integrate(sq, 0, 10, 4) == 2.5 * sum([0, 2.5*2.5, 5*5, 7.5*7.5])

"""
Vraag 1:
    Dit komt omdat er altijd witte vlakken over blijven op deze manier. Je zult dus nooit een perfect gevulde driehoek krijgen.
"""