# wk8ex1.py
# Practicum 8
#
# Naam:
#

# laat deze importregel staan...
from png import *


#
# een testfunctie...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = PNGImage(300, 200)  # maak een afbeelding met width=300, height = 200

    # Geneste lussen!
    for r in range(200):  # lust over de rijen met lusvariabele r
        for c in range(300):  # lust over de kolommen met c
            if c == r:
                im.plot_point(c, r, (255, 0, 0))
            # else:
            #    im.plot_point( c, r, (255,0,0))

    im.save_file()

#
# zet je functies van Practicum 8 hieronder neer:
#


def mult(c, n):
    """Mult uses only a loop and addition
        to multiply c by the positive integer n
    """
    result = 0
    for i in range(n):
        result += c
    return result


def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
        for a total of n times. It returns the final z.
    """
    z = 0
    for i in range(n):
        z = z**2 + c
    return z


def in_mset(c, n):
    z = 0
    for i in range(0, n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True


def we_want_this_pixel(col, row):
    """This function returns True if we want to show
        the pixel at col, row and False otherwise.
    """
    if col % 10 == 0 and row % 10 == 0:
        # Schrijft veel pixels in lijnen waardoor je lijnen krijgt ipv stippen
        return True
    else:
        return False


def test():
    """This function demonstrates how
        to create and save a PNG image.
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # maak een lus om wat pixels te tekenen

    for col in range(width):
        for row in range(height):
            if we_want_this_pixel(col, row):
                image.plot_point(col, row)

    # we hebben door alle pixels gelust; nu schrijven we het bestand

    image.save_file()
