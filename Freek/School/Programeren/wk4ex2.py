#Naam: Freek van Witzenburg
#Probleem: Caeser op Orde!
#Bestandsnaam wk4ex2.py

from collections import Counter

def encipher(s, n):
 """
 """
 if s == "":
     return""
 else:
    return rot(s[0], n) + encipher(s[1:], n)
def rot(c, n):
 """
 """
 if c in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
    return chr(ord(c) + (n % 26))
 else:
    return c
def decipher(s):
 """
 """
 LC = [encipher(s, n) for n in range(26)]
 LoL = [[decipher(s), s] for s in LC]
 bestpair = max(LoL)
 return bestpair[1]
def count(e, L):
 """
 """
 LC = [1 for x in L if x == e]
 return sum(LC)
def blsort(L):
 """
 """
 if len(L) == 0:
    return ""
 else:
    return [0]*count(0, L) + [1]*count(1, L)
def gensort(L):
 """
 """
 L2 = [min(L) for x in L]
 if len(L) == 0:
    return L2
 else:
    return L[1:]
def lingo(s, t):
 """
 """
 if s == "" or t == "":
    return 0
 else:
    return sum((Counter(s) & Counter(t)).values())
def exact_change(target_amount, L):
 """
 """
 if target_amount < 0:
    return False
 elif sum(L) >= target_amount:
    return True
 else:
    return False
def lcs(s, t):
 """
 """
 if s == "" or t == "":
    return ""
 if s[0] == t[0]:
    return s[0] + lcs(s[1:], t[1:])
 result1 = lcs(s[1:], t)
 result2 = lcs(s, t[1:])
 if len(result1) > len(result2):
    return result1
 else:
    return result2
