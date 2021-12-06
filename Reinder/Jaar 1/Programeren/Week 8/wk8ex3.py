#Bestandsnaam: wk8ex3.py
# Namen: Freek van Witzenburg , Bas Mellens, Reinder Noormans

import random
import math


def throw_dart():
    '''
    Deze functie gooit een dart op een bord in een vierkant van 1x1

    output: bool
    '''
    x = random.uniform(-1.0, 1.0)  # zet parameters voor x waarde
    y = random.uniform(-1.0, 1.0)  # zet parameters voor y waarde
    wortel = x**2*y**2

    valpunt = math.sqrt(wortel)
    return valpunt <= .5


def for_pi(n):
    '''
    Deze functie gooit n aantal keer een dart op een vierkant van 1x1

    output: float
    '''
    raak = 0  # geeft het true of false
    worpen = 0
    pi = 0
    for x in range(n):
        worpen += 1  # geeft een plus 1 op aantal worpen
        hit = throw_dart()
        if hit:
            raak += 1  # als de worp raak is geeft hij een true waarde
        else:
            raak += 0  # als de worp raak is geeft hij een false waarde
        pi = (4*raak) / worpen
        print(raak, 'raak van', worpen, 'worpen dus pi is', pi)
    return pi


def while_pi(error):
    '''
    Deze functie blijft pi zoeken door darten te gooien op een vierkant van 1x1.
    Dit word gedaan met een fout marge van 'error'

    output: Int
    '''
    raak = 0
    worpen = 0
    pi = 0
    while not pi < math.pi+error or not pi > math.pi-error:
        worpen += 1  # geeft een plus 1 op aantal worpen
        hit = throw_dart()
        if hit:
            raak += 1  # als de worp raak is geeft hij een true waarde
        else:
            raak += 0  # als de worp raak is geeft hij een false waarde
        pi = (4*raak) / worpen
        print(raak, 'raak van', worpen, 'worpen dus pi is', pi)
    return worpen
