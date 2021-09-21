from math import *

def dbl(x):
    """
    Returns twice the argument

    Spam is great, and dbl("spam") is better!

    :param x: The value to double
    :type x: int, float or string
    """
    return 2 * x

def tpl(x):
    """
    Returns thrice the argument

    :param x: The value to triple
    :type x: int, float or string
    """
    return 3 * x

def sq(x):
    """
    Returns the argument times itself
    
    :param x: The value to itself
    :type x: int or float
    """
    return x*x

def interp(low, hi, fraction):
    """
    Returns the fraction of the difference between low and hi.

    param low: the lowest value in the list
    type low: int or float

    param hi: the highest value in the list
    type hi: int or float

    param fraction: the percentage(0.00-1.00) of difference between low and high
    type fraction: int or float
    """
    return (hi-low)*fraction

def checkends(s):
    """
    returns True if the first letter in the string is the same as the last letter in the string

    param s: The string
    type s: string
    """
    return s[0] == s[-1]

def flipside(s):
    """
    returns the string with it's 2 halfs on the other side.

    param s: the string you want to swap
    type s: string
    """
    lengte = len(s)
    
    if lengte%2 == 0:
       flipped = s[lengte//2:] + s[:-(lengte//2)]
    else:
       flipped = s[lengte//2:] + s[:-(lengte//2)-1]
    return flipped

def convert_from_seconds(s):
    """
    returns the time in days, hours, minutes and seconds from a seconds value(s)

    param s: time in seconds that need to be converted
    type s: int or float
    """
    days = s // (24*60*60)
    s = s % (24*60*60)
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s // (60)
    seconds = s % (60)

    return [days, hours, minutes, seconds]