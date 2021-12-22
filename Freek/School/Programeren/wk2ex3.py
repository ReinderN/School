# Programmeren I, Week 2 Opgave 3
# Bestandsnaam: wk2ex3.py
# Naam: Freek van Witzenburg 
# Problemomschrijving: Feest met functies!

def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # als lege string of lege lijst
        return 0
    return 1 + leng(s[1:])

def mult(n, m):
    """mult returns n times m
        
        param n: een van de variablen die keer de lijst van m gaat
        type n: int or float
        param m: De anderere variablen die keer n bij m
        type m: int or float
        rtype: int or float
    """
    if n == 1:
        return m
    if n == -1:
        return -m
    if n > 0:
        return m + mult(n-1, m)
    if n <= 0:
        return -m + mult(n+1, m)       
        return -m + mult(n+1, m)

def dot(L, k):
    '''dot  geeeft terug waar de index de letter l en k vind
        L and k moeten in de dezelfde index zijn
        param L: de eerste lijst
        type L: lijst
        param k: de tweede lijst
        type k: lijst
        rtype: int or float
    '''
    if len(L) != len(k):
        return 0.0
    if L == [] and k == []:
        return 0.0
    return L[0] * k[0] + dot(L[1:], k[1:])

def ind(e, L):
    """ind komt terug met de index waar je de letter e of l vind
#tests
        param e: het item dat je wilt vinden in een string of lijst
        type e: any
        param L: de lijst van de string waar je de letter L kan vinden
        type L: list or string
        rtype: int
    """
    if e == L[0]:
        return 0
    if e in L:
        return 1 + ind(e, L[1:])
    return len(L)

def letter_score(let):
    """letter_score brengt de score terug op de letter
        
        param let: de letter waarvan de score wil weten
        type: string
        rtype: int
    """
    if let in "adeinorst":
        return 1
    if let in "ghl":
        return 2
    if let in "bcmp":
        return 3
    if let in "kuvjwm":
        return 4
    if let in "f":
        return 5
    if let in "z":
        return 6
    if let in "xy":
        return 8
    if let in "q":
        return 10
    return 0

def scrabble_score(s):
    """scrabble_score brengt de score terug naar een woord
        param s: Het woord waarvan je de score wil weten
        type s: string
        rtype: int
    """
    if s ==  "":
        return 0
    return letter_score(s[0]) + scrabble_score(s[1:])

def transcribe(s):
    """transcribe Brengt terug naar een RNA naar een DNA strings
        param s: DNA string die naar een RNA string wil maken
        type s: String
        rtype: String
    """
    if len(s) == 0:
        return ''
    if s[0] == 'A':
        return 'U' + transcribe(s[1:])
    if s[0] == 'C':
        return 'G' + transcribe(s[1:])
    if s[0] == 'G':
        return 'C' + transcribe(s[1:])
    if s[0] == 'T':
        return 'A' + transcribe(s[1:])
    return '' + transcribe(s[1:])

# Tests mult
if mult(6, 7) != 42:
    raise AssertionError
if mult(6, -7) != -42:
    raise AssertionError
if mult(-6, 7) != -42:
    raise AssertionError
if mult(-6, -7) != 42:
    raise AssertionError
if mult(6, 0) != 0:
    raise AssertionError
if mult(0, 7) != 0:
    raise AssertionError
if mult(0, 0) != 0:
    raise AssertionError
if mult(0, 0) != 0:
    raise AssertionError

# Tests dot
if dot([5, 3], [6, 4]) != 42.0:
    raise AssertionError
if dot([1, 2, 3, 4], [10, 100, 1000, 10000]) != 43210.0:
    raise AssertionError
if dot([5, 3], [6]) != 0.0:
    raise AssertionError
if dot([], [6]) != 0.0:
    raise AssertionError
if dot([], []) != 0.0:
    raise AssertionError

# Tests ind
if ind(42, [55, 77, 42, 12, 42, 100]) != 2:
    raise AssertionError
if ind(42, list(range(0, 100))) != 42:
    raise AssertionError
if ind("hoi", ["hallo", 42, True]) != 3:
    raise AssertionError
if ind("hoi", ["oh", "hoi", "daar"]) != 1:
    raise AssertionError
if ind("i", "team") != 4:
    raise AssertionError
if ind(" ", "nader onderzoek") != 5:
    raise AssertionError

# Tests letter_score
if letter_score('a') != 1:
    raise AssertionError
if letter_score('x') != 8:
    raise AssertionError
if letter_score('d') != 1:
    raise AssertionError
if letter_score('h') != 2:
    raise AssertionError
if letter_score('e') != 1:
    raise AssertionError
if letter_score('g') != 2:
    raise AssertionError
if letter_score('p') != 3:
    raise AssertionError

# Tests scrabble_score
if scrabble_score("quotums") != 24:
    raise AssertionError
if scrabble_score("jacquet") != 24:
    raise AssertionError
if scrabble_score("pyjama") != 20:
    raise AssertionError
if scrabble_score("abcdefghijklmnopqrstuvwxyz") != 84:
    raise AssertionError
if scrabble_score("?!@#$%^&*()") != 0:
    raise AssertionError
if scrabble_score("") != 0:
    raise AssertionError

# Tests transcribe
if transcribe('ACGTTGCA') != 'UGCAACGU':
    raise AssertionError
if transcribe('ACG TGCA') != 'UGCACGU':
    raise AssertionError
if transcribe('GATTACA') != 'CUAAUGU':
    raise AssertionError
if transcribe('hanze') != '':
    raise AssertionError
if transcribe('') != '':
    raise AssertionError