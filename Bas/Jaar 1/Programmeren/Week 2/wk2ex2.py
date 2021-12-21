def dbl(x):
    '''Verdubbelt imput'''
    return 2 * x

def tpl(x):
    '''Verdriedubbelt imput'''
    return 3 * x

def sq(x):
    '''kwadrateert imput'''
    return x**2

def interp(low, hi, fraction):
    '''Kijkt wat het procent (faction) is dat tussen hi en low ligt'''
    return low + fraction * (hi-low)

def checkends(s):
    '''Kijkt of eerste en laatste letter van imput gelijk aan elkaar zijn'''
    if s[0] == s[-1]:
        return True
    return False

def flipside(s):
    '''Split imput doormidden en plakt deel 1 achter deel 2'''
    x = len(s) // 2
    return s[x:] + s[:x]

def convert_from_seconds(s):
    '''Convert seconden naar dagen uren minuten en seconden'''
    days = s // (24 * 60 * 60)
    s = s % (24 * 60 * 60)

    hours = s // (60 * 60)
    s = s % (60 * 60)

    minutes = s // 60
    s = s % 60

    return [days, hours, minutes, s]