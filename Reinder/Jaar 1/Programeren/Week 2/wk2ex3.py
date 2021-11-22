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
    """mult returns n times m
        
        param n: one of the values to times by m
        type n: int or float

        param m: the other value that times n by m
        type m: int or float

        rtype: int or float
    """
    if n == 1:
        return m
    elif n == -1:
        return -m
    elif n > 0:
        return m + mult(n-1, m)
    elif n <= 0:
        return -m + mult(n+1, m)

def dot(L, k):
    '''dot returns every item of L times the the same indexeded item of k
        L and k need to have the same indexes

        param L: the first list
        type L: list

        param k: the second list
        type k: list

        rtype: int or float
    '''
    if len(L) != len(k):
        return 0.0
    elif L == [] and k == []:
        return 0.0
    else:
        return L[0] * k[0] + dot(L[1:], k[1:])

def ind(e, L):
    """ind returns the index where e is in L

        param e: the item you want to find in the list or string(L)
        type e: any

        param L: the list or string you want to find e in
        type L: list or string

        rtype: int
    """
    if e == L[0]:
        return 0
    elif e in L:
        return 1 + ind(e, L[1:])
    else:
        return len(L)

def letter_score(let):
    """letter_score returns the score of a letter
        
        param let: the letter you want to know the score of
        type: string

        rtype: int
    """
    if let in "adeinorst":
        return 1
    elif let in "ghl":
        return 2
    elif let in "bcmp":
        return 3
    elif let in "kuvjwm":
        return 4
    elif let in "f":
        return 5
    elif let in "z":
        return 6
    elif let in "xy":
        return 8
    elif let in "q":
        return 10
    else:
        return 0
    
def scrabble_score(s):
    """scrabble_score returns the score of an entire word

        param s: the word that you want to know the score from
        type s: string

        rtype: int
    """
    if s ==  "":
        return 0
    else:
        return letter_score(s[0]) + scrabble_score(s[1:])

def transcribe(s):
    """transcribe returns RNA from a DNA string(s)

        param s: DNA string you want to transform to RNA
        type s: String

        rtype: String
    """
    if len(s) == 0:
        return ''
    elif s[0] == 'A':
        return 'U' + transcribe(s[1:])
    elif s[0] == 'C':
        return 'G' + transcribe(s[1:])
    elif s[0] == 'G':
        return 'C' + transcribe(s[1:])
    elif s[0] == 'T':
        return 'A' + transcribe(s[1:])
    else:
        return '' + transcribe(s[1:])

# Tests mult
assert mult(6, 7) == 42
assert mult(6, -7) == -42
assert mult(-6, 7) == -42
assert mult(-6, -7) == 42
assert mult(6, 0) == 0
assert mult(0, 7) == 0
assert mult(0, 0) == 0

# Tests dot
assert dot([5, 3], [6, 4]) == 42.0
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6]) == 0.0
assert dot([], [6]) == 0.0
assert dot([], []) == 0.0

# Tests ind
assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100))) == 42
assert ind("hoi", ["hallo", 42, True]) == 3
assert ind("hoi", ["oh", "hoi", "daar"]) == 1
assert ind("i", "team") == 4
assert ind(" ", "nader onderzoek") == 5

# Tests letter_score
assert letter_score('a') == 1
assert letter_score('x') == 8
assert letter_score('d') == 1
assert letter_score('h') == 2
assert letter_score('e') == 1
assert letter_score('g') == 2
assert letter_score('p') == 3

# Tests scrabble_score
assert scrabble_score("quotums") == 24
assert scrabble_score("jacquet") == 24
assert scrabble_score("pyjama") == 20
assert scrabble_score("abcdefghijklmnopqrstuvwxyz") == 84
assert scrabble_score("?!@#$%^&*()") == 0
assert scrabble_score("") == 0

# Tests transcribe
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU'  # De spatie verdwijnt
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('hanze')    == ''         # Andere tekens verdwijnen
assert transcribe('')         == ''