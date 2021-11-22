#
# wk7ex1c.py - uniekheid controleren  (voor de random-number generator in Hmmm)
#    De functie test(s) staat hier al in (onderaan).
#
# Namen: L.P.R. Noordmans, B. Mellens, F.M. van Witzenburg
#
# Je plakt je 100 getallen in deze triple-quoted string:
NUMBERS = """
3
42
47
46
91
5
"""


def unique(L):
    """
    This should be your uniqueness-tester, written for week 7
    Usually, it uses the recursive pattern:

    if ...      # handle base case
    elif ...    # check whether L[0] re-appears
    else ...    # otherwise...
    """
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return unique(L[1:])


def test(s):
    """test accepts a triple-quoted string, s,
        containing one number per line. Then, test
        returns True if those numbers are all unique
        (or if s is empty); otherwise it returns False
    """
    s = s.strip()                 # haal alle spaties aan het begin en eind van s weg
    list_of_strings = s.split()   # splits s op elke spatie en nieuwe regel
    # print("list_of_strings is", list_of_string)
    # converteer ze allemaal naar ints
    list_of_integers = [int(s) for s in list_of_strings]
    # print("list_of_integers is", list_of_integers)
    return unique(list_of_integers)


# Uitproberen!
result = test('''91
20
29
18
87
36
65
74
63
32
81
10
19
8
77
26
55
64
53
22
71
0
9
98
67
16
45
54
43
12
61
90
99
88
57
6
35
44
33
2
51
80
89
78
47
96
25
34
23
92
41
70
79
68
37
86
15
24
13
82
31
60
69
58
27
76
5
14
3
72
21
50
59
48
17
66
95
4
93
62
11
40
49
38
7
56
85
94
83
52
1
30
39
28
97
46
75
84
73
42''') # gedaan met a=21, c=9, m=100, seed=42 && N=100
print("\nTest op uniekheid:  Het resultaat is", result)
