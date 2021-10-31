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

def rle(input_string):
    """ takes input as string and checks repeating bit
        return repeating bit with their counts. """
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
    	    if prev:
                entry = (prev,count)
        lst.append(entry)
        #print lst
        count = 1
        prev = character
    else:
        count += 1
        
    else:
        entry = (character,count)
        lst.append(entry)
        eturn lst

def new_dict(s):
            """ input of rle(S) i.e., tuples of bit and repeating counts
                output dict as bit as key and value as counts with binary conversion.
            """  

            dict=rle(s)
            new_dict = []
            temp = []
            for k,v in dict:
                temp = k + "%07d" % int(bin(v)[2:])
                new_dict.append(temp)
            return new_dict

def compress(s):
 """ takes a binary string s of length less than or equal to 64 as 
input and returns another binary string as output."""
            
 l = new_dict(s)
 return''.join(str(elem) for elem in l)

def uncompress (c):
    """"""