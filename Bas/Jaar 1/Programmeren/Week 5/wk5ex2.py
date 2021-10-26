def num_to_base_b(n, b):
    """num_to_base_b accepts a integer n and a base b between (2-10)
        and returns a string representing the numbere n in base b.
    """
    if n == 0:
        return""
    elif n % b == 1:
        return num_to_base_b(n // b, b) +"1"
    elif n % b == 2:
        return num_to_base_b(n // b, b) + "2"
    elif n % b == 3:
        return num_to_base_b(n // b, b) + "3"
    elif n % b == 4:
        return num_to_base_b(n // b, b) + "4"
    elif n % b == 5:
        return num_to_base_b(n // b, b) + "5"
    elif n % b == 6:
        return num_to_base_b(n // b, b) + "6"
    elif n % b == 7:
        return num_to_base_b(n // b, b) + "7"
    elif n % b == 8:
        return num_to_base_b(n // b, b) + "8"
    elif n % b == 9:
        return num_to_base_b(n // b, b) + "9"
    elif n % b == 10:
        return num_to_base_b(n // b, b) + "10"
    else:
        return num_to_base_b(n // b, b) + "0"

assert num_to_base_b(0, 4) == ''
assert num_to_base_b(42, 5) == '132'
assert num_to_base_b(4, 2) == '100'

def 