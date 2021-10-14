# Programmeren I, Practicum 5
# Bestandsnaam: wk5ex1
# Naam: Reinder Noordmans
# Probleemomschrijving: conversie binair <-> decimaal

def is_odd(n):
    if n%2 == 0:
        return False
    else:
        return True

def num_to_binary(n):
    if n == 0:
        return ""
    elif n % 2 == 1:
        return num_to_binary(n//2) + "1"
    else:
        return num_to_binary(n//2) + "0"

def binary_to_num(s):
    """
    """
    if s == "":
        return 0

    elif s[-1] == "1":
        return 2*binary_to_num(s[:-1]) + 1

    else:
        return 2*binary_to_num(s[:-1]) + 0

def increment(S):
    if isinstance(S, int):
        n = S
    else:
        n = binary_to_num(S)
    x = n + 1
    y = num_to_binary(x)
    leny = len(y)
    if leny > 8:
        nleny = leny -8
        return y[nleny:]
    else:
        ny = "0"*8+y
        nleny = len(ny) -8
        return ny[nleny:]

def count(s,n):
    for x in range(n):
        print(increment(int(s)+x))


assert binary_to_num("") == 0
assert binary_to_num("101010") == 42

assert num_to_binary(0) == ""
assert num_to_binary(42) == "101010"    

assert not is_odd(42)
assert is_odd(43)