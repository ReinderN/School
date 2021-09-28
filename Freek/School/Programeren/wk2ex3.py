# Programmeren I, Week 2 Opgave 3
# Bestandsnaam: wk2ex3.py
# Naam:
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