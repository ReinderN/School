def num_to_base_b(n, b):
    '''
    num_to_base_b takes an non negative number(n) and converts it to another base(b)

    n = int number you want to convert to base
    b = the base you want the number to be converted to

    returns: Str
    '''

    new_n = n//b

    if n == 0:
        return ''
    elif n % b == 1:
        return num_to_base_b(new_n, b) + '1'
    elif n % b == 2:
        return num_to_base_b(new_n, b) + '2'
    elif n % b == 3:
        return num_to_base_b(new_n, b) + '3'
    elif n % b == 4:
        return num_to_base_b(new_n, b) + '4'
    elif n % b == 5:
        return num_to_base_b(new_n, b) + '5'
    elif n % b == 6:
        return num_to_base_b(new_n, b) + '6'
    elif n % b == 7:
        return num_to_base_b(new_n, b) + '7'
    elif n % b == 8:
        return num_to_base_b(new_n, b) + '8'
    elif n % b == 9:
        return num_to_base_b(new_n, b) + '9'
    else:
        return num_to_base_b(new_n, b) + '0'


def base_b_to_num(s, b):
    '''
    base_b_to_num converts a base from 2 to 10 into a decimal num

    s = string in base
    b = the base the string is

    returns: Int
    '''

    new_s = s[:-1]

    if s == '':
        return 0
    elif b >= 1 and s[-1] == '1':
        return b*base_b_to_num(new_s, b) + 1
    elif b >= 2 and s[-1] == '2':
        return b*base_b_to_num(new_s, b) + 2
    elif b >= 3 and s[-1] == '3':
        return b*base_b_to_num(new_s, b) + 3
    elif b >= 4 and s[-1] == '4':
        return b*base_b_to_num(new_s, b) + 4
    elif b >= 5 and s[-1] == '5':
        return b*base_b_to_num(new_s, b) + 5
    elif b >= 6 and s[-1] == '6':
        return b*base_b_to_num(new_s, b) + 6
    elif b >= 7 and s[-1] == '7':
        return b*base_b_to_num(new_s, b) + 7
    elif b >= 8 and s[-1] == '8':
        return b*base_b_to_num(new_s, b) + 8
    elif b >= 9 and s[-1] == '9':
        return b*base_b_to_num(new_s, b) + 9
    else:
        return b*base_b_to_num(new_s, b) + 0


def base_to_base(b1, b2, s_in_b1):
    '''
    converts a base into another base

    b1 = the base the string is in
    b2 = the base you want to convert to
    s_in_b1 = the string that needs to be converted to another b

    returns: Str
    '''

    num = base_b_to_num(s_in_b1, b1)
    return num_to_base_b(num, b2)


def add(s, t):
    '''
    adds to binary numbers together

    s: the first binary number
    t: the second binary number

    returns: Str
    '''

    num1 = base_b_to_num(s, 2)
    num2 = base_b_to_num(t, 2)
    calc = num1 + num2
    return num_to_base_b(calc, 2)


def add_b(s, t):
    '''
    add_b adds to binary numbers together

    s: the first binary number
    t: the second binary number

    returns: Str
    '''
    if len(s) == 0:
        return t
    elif len(t) == 0:
        return s

    if s[-1] == '0' and t[-1] == '0':
        return add_b(s[:-1], t[:-1]) + '0'
    elif s[-1] == '1' and t[-1] == '0':
        return add_b(s[:-1], t[:-1]) + '1'
    elif s[-1] == '0' and t[-1] == '1':
        return add_b(s[:-1], t[:-1]) + '1'
    elif s[-1] == '1' and t[-1] == '1':
        carry = add_b("1", s[:-1])
        return add_b(carry, t[:-1]) + '0'


assert num_to_base_b(9944, 2) == '10011011011000'
assert num_to_base_b(144556, 3) == '21100021221'
assert num_to_base_b(15, 4) == '33'
assert num_to_base_b(56, 5) == '211'
assert num_to_base_b(53, 6) == '125'
assert num_to_base_b(145, 7) == '265'
assert num_to_base_b(555, 8) == '1053'
assert num_to_base_b(7856, 9) == '11688'
assert num_to_base_b(1455, 10) == '1455'

assert base_b_to_num('10011011011000', 2) == 9944
assert base_b_to_num('21100021221', 3) == 144556
assert base_b_to_num('33', 4) == 15
assert base_b_to_num('211', 5) == 56
assert base_b_to_num('125', 6) == 53
assert base_b_to_num('265', 7) == 145
assert base_b_to_num('1053', 8) == 555
assert base_b_to_num('11688', 9) == 7856
assert base_b_to_num('1455', 10) == 1455

assert base_to_base(2, 3, '10011011011000') == '111122022'
assert base_to_base(3, 4, '21100021221') == '203102230'
assert base_to_base(4, 5, '33') == '30'
assert base_to_base(5, 6, '211') == '132'
assert base_to_base(6, 7, '125') == '104'
assert base_to_base(7, 8, '265') == '221'
assert base_to_base(8, 9, '1053') == '676'
assert base_to_base(9, 10, '11688') == '7856'
assert base_to_base(10, 2, '1455') == '10110101111'

assert add('10101', '101001') == '111110'
assert add('10001', '1001011') == '1011100'
assert add('10011101', '11') == '10100000'
assert add('1', '10') == '11'
assert add('1001', '1001') == '10010'

assert add_b('10101', '101001') == '111110'
assert add_b('10001', '1001011') == '1011100'
assert add_b('10011101', '11') == '10100000'
assert add_b('1', '10') == '11'
assert add_b('1001', '1001') == '10010'
