def list_to_str(L):
    """L must be a list of characters;
       this function returns a single string made from them.
    """
    if len(L) == 0:
        return ""
    return L[0] + list_to_str(L[1:])

def rot(c, n):
    """rotates the character(c) with n places using the ceasar method.

    c: single character to be rotaded
    n: amount of steps it should rotate
    """
    cplace = ord(c)
    cplace += n
    if not 'A' <= c <= 'Z' and not 'a' <= c <= 'z':
        cplace -= n
    elif cplace > 122:
        cplace -= 26
    elif cplace > 90 and c < 'a':
        cplace -= 26
    new_c = chr(cplace)
    return new_c

def encipher(s,n):
    """encrypts the string(s) using the ceasar method with steps of n.
    
    s: the string you want to encrypt
    n: the amount of steps(non negative) you want to take to encrypt the string(s)
    """
    L = [rot(x, n) for x in s]
    encrypted = list_to_str(L)
    return encrypted

def letter_prob(c):
    """If c is an alphabetic character,
       we return its monogram probability (for Dutch),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       https://www.sttmedia.com/characterfrequency-nederlands
    """
    if c == 'e' or c == 'E':
        return 0.1909
    if c == 'n' or c == 'N':
        return 0.0991
    if c == 'a' or c == 'A':
        return 0.0769
    if c == 't' or c == 'T':
        return 0.0642
    if c == 'i' or c == 'I':
        return 0.0630
    if c == 'o' or c == 'O':
        return 0.0581
    if c == 'r' or c == 'R':
        return 0.0562
    if c == 'd' or c == 'D':
        return 0.0541
    if c == 's' or c == 'S':
        return 0.0384
    if c == 'l' or c == 'L':
        return 0.0380
    if c == 'h' or c == 'H':
        return 0.0312
    if c == 'g' or c == 'G':
        return 0.0312
    if c == 'k' or c == 'K':
        return 0.0279
    if c == 'm' or c == 'M':
        return 0.0256
    if c == 'v' or c == 'V':
        return 0.0224
    if c == 'u' or c == 'U':
        return 0.0212
    if c == 'j' or c == 'J':
        return 0.0182
    if c == 'w' or c == 'W':
        return 0.0172
    if c == 'z' or c == 'Z':
        return 0.0160
    if c == 'p' or c == 'P':
        return 0.0149
    if c == 'b' or c == 'B':
        return 0.0136
    if c == 'c' or c == 'C':
        return 0.0130
    if c == 'f' or c == 'F':
        return 0.0073
    if c == 'y' or c == 'Y':
        return 0.0006
    if c == 'x' or c == 'X':
        return 0.0005
    if c == 'q' or c == 'Q':
        return 0.0001
    return 1.0

def score(s):
    """score counts the total point of each character in the string(s)

    s: the string you want to know the score from
    """
    scorepoints = [letter_prob(c) for c in s]
    spoints = sum(scorepoints)
    return [spoints, s]

def decipher(s):
    """Tries to decipher the string(s) using the ceasar method

    s: string you want to decrypt
    """
    String_List = [encipher(s, n) for n in range(26)]
    points = [score(s) for s in String_List]
    return max(points)[1]

assert encipher("xyza", 1) == "yzab"
assert encipher("Z A", 1) == "A B"
assert encipher('*ab?', 1) == '*bc?'
assert encipher('Dit is een string!', 1) == 'Eju jt ffo tusjoh!'
assert encipher('Caesarcijfer? Ik heb liever Caesarsalade.', 25) == 'Bzdrzqbhiedq? Hj gda khdudq Bzdrzqrzkzcd.'

assert decipher('Bzdrzqbhiedq? Hj gda khdudq Bzdrzqrzkzcd.') == 'Caesarcijfer? Ik heb liever Caesarsalade.'
assert decipher('Aadxas ue exqotfe pq haadflqffuzs hmz baxufuqw yqf mzpqdq yuppqxqz.') == 'Oorlog is slechts de voortzetting van politiek met andere middelen.'
assert decipher('Wjnsijw Sttwirfsx') == 'Reinder Noordmans'