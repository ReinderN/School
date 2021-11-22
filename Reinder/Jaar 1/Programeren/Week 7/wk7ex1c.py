#
# wk7ex1c.py - uniekheid controleren  (voor de random-number generator in Hmmm)
#    De functie test(s) staat hier al in (onderaan).
#
# Naam:
#
# Je plakt je 100 getallen in deze triple-quoted string:
NUMBERS = """
3
42
47
46
91
5
"""


def unique(L):
    """
    This should be your uniqueness-tester, written for week 7
    Usually, it uses the recursive pattern:

    if ...      # handle base case
    elif ...    # check whether L[0] re-appears
    else ...    # otherwise...
    """
    return False     # dummycode


def test(s):
    """test accepts a triple-quoted string, s,
       containing one number per line. Then, test
       returns True if those numbers are all unique
       (or if s is empty); otherwise it returns False
    """
    s = s.strip()                 # haal alle spaties aan het begin en eind van s weg
    list_of_strings = s.split()   # splits s op elke spatie en nieuwe regel
    # print("list_of_strings is", list_of_string)
    list_of_integers = [int(s) for s in list_of_strings]  # converteer ze allemaal naar ints
    # print("list_of_integers is", list_of_integers)
    return unique(list_of_integers)


# Uitproberen!
result = test(NUMBERS)
print("\nTest op uniekheid:  Het resultaat is", result)
