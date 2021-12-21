#
# wk7ex5.py - Aan de slag met lussen!
#
# Naam: L.P.R. Noordmans, B. Mellens, F.M. van Witzenburg
#

import random


def fac(n):
    """Loop-based factorial function
        Argument: a nonnegative integer, n
        Return value: the factorial of n
    """
    result = 1                 # beginwaarde; lijkt op een basisgeval
    for x in range(1, n + 1):  # herhaal van 1 tot en met n
        result = result * x    # pas het resultaat aan door keer x te doen
    return result              # merk op dat dit NA de lus is!


def power(b, p):
    """Loop-based function 
        b to the power of p

        b: int
        p: int
    """
    result = 1
    for x in range(p):
        result *= b
    return result


def summed(L):
    """Loop-based function to return a numeric list.
        ("sum" is built-in, so we're using a different name.)
        Argument: L, a list of integers.
        Result: the sum of the list L.
    """
    result = 0
    for e in L:
        result = result + e    # of result += e
    return result


def summed_odds(L):
    ''' returns the sum of all the odd intergers in a list(L)

        L = list
    '''
    som = 0
    for x in L:
        if x % 2 == 1:
            som += x
    return som


def count_guesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.
        Argument: hidden, a "hidden" integer from 0 to 99.
        Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 tot en met 99
    num_guesses = 1                          # we hebben nu 1 keer geraden
    while guess != hidden:
        guess = random.choice(range(0, 100))  # opnieuw raden!
        num_guesses += 1                     # 1 toevoegen aan het aantal pogingen
    return num_guesses


def unique(L):
    """Returns whether all elements in L are unique.
        Argument: L, a list of any elements.
        Return value: True, if all elements in L are unique,
        or False, if there is any repeated element
    """
    if len(L) == 0:
        return True
    if L[0] in L[1:]:
        return False
    return unique(L[1:])  # in deze functie mag je WEL recursie gebruiken!


def until_a_repeat(high):
    '''Continues generating numbers between 0 and high untill it generates the same number twice

        high = int
    '''
    L = []
    count = 0
    while unique(L):
        guess = random.choice(range(0, high))
        L += [guess]
        count += 1
    return count


# Tests
assert fac(10) == 3628800
assert fac(15) == 1307674368000
assert fac(6) == 720

assert power(4, 5) == 1024
assert power(8, 10) == 1073741824
assert power(6, 4) == 1296

assert summed([6, 9, 8, 4, 2, 0, 6, 9]) == 44
assert summed([46, 4798, 6455, 32]) == 11331
assert summed([968, 465, 65, 6]) == 1504

assert summed_odds([6, 9, 8, 4, 2, 0, 6, 9]) == 18
assert summed_odds([46, 4798, 6455, 32]) == 6455
assert summed_odds([968, 465, 65, 6]) == 530
