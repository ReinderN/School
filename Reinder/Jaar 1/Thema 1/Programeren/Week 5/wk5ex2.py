# Gemaakt door: Reinder Noordmans, Bas Mellens, Freek van Witzenburg

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


def counter(s):
    '''
    counts the amount of times the first character of s is following itself.

    s: the string you want to count
    returns: list; item[0] == the character; item[1] == the amount of times item[0] appears
    '''
    char = s[0]
    count = 0
    for x in s:
        if x == char:
            count += 1
        else:
            return [char, count]
    return [char, count]


def num_to_binary(n):
    """
    num_to_binary changes a non negative number(n) to a binary string

    n: non negative int
    returns: str
    """
    if n == 0:
        return ""
    elif n % 2 == 1:
        return num_to_binary(n//2) + "1"
    elif n % 2 == 0:
        return num_to_binary(n//2) + "0"


def num_to_binary_8bit(n):
    '''
    converts the num_to_binary number to an 8 bit vallue

    n: the num that needs to be in an 8bit string
    returns: Str
    '''
    bits = num_to_binary(n)
    return '0'*(8-len(bits)) + bits


def flattenNestedList(nestedList):
    ''' Converts a nested list to a flat list 
    van: https://thispointer.com/python-convert-list-of-lists-or-nested-list-to-flat-list/
    '''
    flatList = []
    # Iterate over all the elements in given list
    for elem in nestedList:
        # Check if type of element is list
        if isinstance(elem, list):
            # Extend the flat list by adding contents of this element (list)
            flatList.extend(flattenNestedList(elem))
        else:
            # Append the elemengt to the list
            flatList.append(elem)
    return flatList


def compress(s):
    '''
    compresses a binary string

    s: the string that needs to be compressed
    returns: Str
    '''
    compr = ''
    if s == '':
        return ''
    else:
        charcount = counter(s)
        if charcount[0] == '1':
            charcount[1] += 128
            base = num_to_binary_8bit(charcount[1])
            compressed = compress(s[charcount[1]-128:])
            aflat_list = flattenNestedList([base, compressed])
            for x in aflat_list:
                compr += x
            return compr
        else:
            base = num_to_binary_8bit(charcount[1])
            compressed = compress(s[charcount[1]:])
            aflat_list = flattenNestedList([base, compressed])
            for x in aflat_list:
                compr += x
            return compr


def binary_to_num(s):
    """
    binary_to_num changes a binary string(s) to an int number

    s: str
    returns: int
    """
    if s == "":
        return 0

    elif s[-1] == "1":
        return 2*binary_to_num(s[:-1]) + 1

    else:
        return 2*binary_to_num(s[:-1]) + 0


def uncompresser(s):
    '''
    uncrompresses 8 binary bits

    s: the 8 bit string that needs to be uncompressed
    returns: Str
    '''
    if s[0] == '0':
        return '0'*binary_to_num(s[1:])
    else:
        return '1'*binary_to_num(s[1:])


def uncompress(c):
    '''
    uncompresses an binary string

    c: the string that needs to be uncompressed
    returns: the uncompressed string
    '''
    unc = ''
    lenght = len(c)//8
    for x in range(lenght):
        unc += uncompresser(c[x*8:(x+1)*8])
    return unc


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

assert compress('1'*50 + '0'*120+'1'*10) == '101100100111100010001010'
assert compress('1111101') == '100001010000000110000001'
assert compress('0'*127+'1'*127) == '0111111111111111'

assert uncompress('101100100111100010001010') == '1'*50 + '0'*120+'1'*10
assert uncompress('100001010000000110000001') == '1111101'
assert uncompress('0111111111111111') == '0'*127+'1'*127
