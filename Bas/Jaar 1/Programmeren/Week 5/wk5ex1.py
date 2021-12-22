# Programmeren I, Practicum 5
# Bestandsnaam: wk5ex1
# Naam: Bas Mellens
# Probleemomschrijving: conversie binair <-> decimaal

def is_odd(n):
    """is_odd checks if a number(n) is odd or not
    
    n: int
    returns: boolean
    """
    if n%2 == 0:
        return False
    return True

def num_to_binary(n):
    """
    num_to_binary changes a non negative number(n) to a binary string

    n: non negative int
    returns: str
    """
    if n == 0:
        return ""
    if n % 2 == 1:
        return num_to_binary(n//2) + "1"
    return num_to_binary(n//2) + "0"

def binary_to_num(s):
    """
    binary_to_num changes a binary string(s) to an int number

    s: str
    returns: int
    """
    if s == "":
        return 0

    if s[-1] == "1":
        return 2*binary_to_num(s[:-1]) + 1
    return 2*binary_to_num(s[:-1]) + 0

def increment(S):
    """
    increment adds 1 to the number value of a binary string(S)

    S: string
    returns: S+1
    """
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
    ny = "0"*8+y
    nleny = len(ny) -8
    return ny[nleny:]

def count(s,n):
    """
    count adds 1 to a binary string(s) a certain number(n) of times

    s: binary string
    n: non negative int
    returns: list of counts
    """
    if n < 0:
        return
    print(s)
    count(increment(s), n-1)

def num_to_ternary(n):
    """
    num_to_ternary changes a non negative number(n) to a ternary string

    n: non negative int
    returns: str
    """
    if n == 0:
        return ""
    if n % 3 == 1:
        return num_to_ternary(n//3) + "1"
    if n % 3 == 2:
        return num_to_ternary(n//3) + "2"
    return num_to_ternary(n//3) + "0"

def ternary_to_num(s):
    """
    ternary_to_num changes a ternary string(s) to an int number

    s: str
    returns: int
    """
    if s == "":
        return 0

    if s[-1] == "1":
        return 3*ternary_to_num(s[:-1]) + 1

    if s[-1] == "2":
        return 3*ternary_to_num(s[:-1]) + 2
    return 3*ternary_to_num(s[:-1]) + 0

def balanced_ternary_to_num(s):
    """
    balanced_ternary_to_num changes a balanced ternary string(s) to an int number

    s: str
    returns: int
    """
    if s == "":
        return 0

    if s[-1] == "+":
        return 3*balanced_ternary_to_num(s[:-1]) + 1

    if s[-1] == "-":
        return 3*balanced_ternary_to_num(s[:-1]) + -1
    return 3*balanced_ternary_to_num(s[:-1]) + 0

def num_to_balanced_ternary(n):
    """
    balanced_num_to_ternary changes a non negative number(n) to a balanced ternary string

    n: non negative int
    returns: str
    """
    if n == 0:
        return ""
    if n % 3 == 1:
        return num_to_balanced_ternary(n//3) + "+"
    if n % 3 == 2:
        return num_to_balanced_ternary((n//3)+1) + "-"
    if n % 3 == 0:
        return num_to_balanced_ternary(n//3) + "0"    

assert is_odd(3)
assert not is_odd(4)
assert is_odd(-3)
assert not is_odd(-4)

assert num_to_binary(5) == '101'
assert num_to_binary(12) == '1100'
assert num_to_binary(100) == '1100100'
assert num_to_binary(5321) == '1010011001001'

assert binary_to_num('101') == 5
assert binary_to_num('1100') == 12
assert binary_to_num('1100100') == 100
assert binary_to_num('1010011001001') == 5321

assert increment('101') == '00000110'
assert increment('1100') == '00001101'
assert increment('1100100') == '01100101'
assert increment('1010011001001') == '11001010'

assert num_to_ternary(5) == '12'
assert num_to_ternary(12) == '110' 
assert num_to_ternary(100) == '10201'
assert num_to_ternary(5321) == '21022002'

assert ternary_to_num('12') == 5
assert ternary_to_num('110') == 12
assert ternary_to_num('10201') == 100
assert ternary_to_num('21022002') == 5321

assert balanced_ternary_to_num('+--') == 5
assert balanced_ternary_to_num('++0') == 12
assert balanced_ternary_to_num('++-0+') == 100
assert balanced_ternary_to_num('+-++0-0+-') == 5321

assert num_to_balanced_ternary(5) == '+--'
assert num_to_balanced_ternary(12) == '++0'
assert num_to_balanced_ternary(100) == '++-0+'
assert num_to_balanced_ternary(5321) == '+-++0-0+-'
