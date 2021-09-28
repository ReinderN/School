# Programmeren I, Week 2 Opgave 3
# Bestandsnaam: wk2ex3.py
# Naam: Reinder Noordmans
# Problemomschrijving: Feest met functies!


#
# voorbeeldfunctie leng uit het college
#

def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # als lege string of lege lijst
        return 0
    else:
        return 1 + leng(s[1:])

def mult(n, m):
    if n == 1:
        return m
    elif n == -1:
        return -m
    elif n > 0:
        return m + mult(n-1, m)
    elif n <= 0:
        return -m + mult(n+1, m)       

#tests
assert mult(6, 7) == 42
assert mult(6, -7) == -42
assert mult(-6, 7) == -42
assert mult(-6, -7) == 42
assert mult(6, 0) == 0
assert mult(0, 7) == 0
assert mult(0, 0) == 0