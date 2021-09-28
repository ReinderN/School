# bestandsnaam: wk2ex2.py
# Naam: Freek van Witzenburg

def dbl(x):
    """Returns twice the argument

    Spam is great, and dbl("spam") is better!

    :param x: The value to double
    :type x: int, float or string
    :rtype: int, float or string
    """
    return 2 * x

def convert_from_seconds(s):
    """Een programma om dagen naar uren naar minuten en seconden te maken
    """
    days = s // (24 * 60 * 60)  # Het aantal dagen
    s = s % (24 * 60 * 60)  # Het restant
    hours = s // (60*60) # het aantal uren
    minutes = s // (60*60/60) # het aantal minuten
    seconds = S // (60/60) #aantal seconden
    return [days, hours, minutes, seconds]





