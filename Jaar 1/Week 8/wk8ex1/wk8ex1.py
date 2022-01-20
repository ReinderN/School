# wk8ex1.py
# Practicum 8
#
# Naam: Freek  van Witzenburg, Reinder Noormans, Bas Melens
#

# laat deze importregel staan...
from png import PNGImage, get_rgb


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
            else:
                im.plot_point(c, r, (255, 0, 0))

    im.save_file()

# zet je functies van Practicum 8 hieronder neer:


def mult(c, n):
    """ de functie mult maakt gebruik van c en vermenigdvuldigd dat  met een postieve interger N.
    """
    result = 0
    for i in range(n):
        result += c
    return result


def update(c, n):
    """Update start met z = 0 en vervolgs doet het programma z = z**2 + c
        voor een het aantal keer N en geeft hierna z terug als resultaat.
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
    """ De functie geeft col terug als deze true is en row als hij False is.
    """
    if col % 10 == 0 and row % 10 == 0:
        # Schrijft veel pixels in lijnen waardoor je lijnen krijgt ipv stippen
        return True
    return False


def test():
    """ Deze functie test of het programma hoe het moet gebruikt worden en of het een png terug geeft.
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


def example():
    """Laat zien hoe een programma een foto importeert en een pixel versie terug geeft.
    """
    input_pixels = get_rgb("./pngs/alien.png")
    input_pixels = input_pixels[::-1]  # de rijen zijn omgekeerd

    height = len(input_pixels)
    width = len(input_pixels[0])
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            if col % 10 < 5 and row % 10 < 5:  # teken maar een deel van de pixels
                image.plot_point(col, row, input_pixels[row][col])

    image.save_file()
