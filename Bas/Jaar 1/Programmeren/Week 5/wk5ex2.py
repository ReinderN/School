def num_to_base_b(n, b):
    """Converts N to a base B number"""
    if n == 0:
        return""
    else:
       return num_to_base_b(n // b, b) + str(n % b)

assert num_to_base_b(0, 4) == ''
assert num_to_base_b(42, 5) == '132'
assert num_to_base_b(4, 2) == '100'

def base_b_to_num(s, b):
    """Returns S in base B"""
    if s == '':
        return 0
    else:
        return base_b_to_num(s[0:-1], b) *b + int(s[-1])

def base_to_base(b1, b2, s_in_b1):
    """Sinb1 is a string of integer in b1 and returns a string with a number in b2"""
    return num_to_base_b(int(base_b_to_num(s_in_b1, b1)), b2)

def add(s, t):
    """Returns the add of two binary strings in binary"""
    return num_to_base_b(int(base_b_to_num(s, 2) + base_b_to_num(t, 2)), 2)

def add_b(s, t):
    """Add two binary values"""
    if len(s) == 0:
        return t
    elif len(t) == 0:
        return s

    if s[-1] == "0" and t[-1] == "0":
        return add_b(s[:-1], t[:-1]) + "0"
    elif s[-1] == "0" and t[-1] == "1":
        return add_b(s[:-1], t[:-1]) + "1"
    elif s[-1] == "1" and t[-1] == "0":
        return add_b(s[:-1], t[:-1]) + "1"
    else:
        carry = add_b("1", s[:-1])
        return add_b(carry, t[:-1]) + "0"

def compress(s):
    """"""