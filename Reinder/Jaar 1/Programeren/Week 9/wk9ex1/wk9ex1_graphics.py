# gebruik start()


# zorg dat dit geïmplementeerd is!
from wk9ex1 import next_life_generation

from turtle import *
from turtlegrid import *
from random import *

# overzicht van toetsen:
print("    PAUZE: 'p'")
print(" DOORGAAN: 'Return'/'Enter'")
print("   WISSEN: 'Spatie'")
print("  SLUITEN: 'Esc'")
print()
print("Begin met start() ...")
print()


# de beginfunctie:
def start(width=20, height=20):
    # de turtle-library starten
    reset()  # wis het scherm
    tracer(False)  # zet de animatie uit
    delay(0)  # teken zo snel mogelijk
    global board, screen
    screen = Screen()
    board = random_cells(width, height)
    screen.listen()
    onscreenclick(life_mouse_handler)
    screen.onkey(show_good_2, "Return")
    screen.onkey(bye, "Escape")
    screen.onkey(blank, "space")
    show(board)
    done()


global board


def all_zeroes(L):
    """Checks if the board is all zeroes"""
    if type(board[0]) == int:  # als het bord maar 1 lijst is...
        return L == [0] * len(L)
    else:  # als het bord een raster is...
        counter = 0
        for k in L:
            if k == [0] * len(k):
                counter += 1
        return counter == len(L)


def show_good():
    """Makes the next life generation appear"""
    global board
    board = next_life_generation(board)
    show(board)


running = True


def show_good_2():
    """Sets the board to keep moving through generations of life.
        Allows for pausing with "p", resuming with "Enter"/"Return",
        and automatically pauses the game if the board stops changing
        or becomes blank."""
    global board
    global running
    screen.onkey(game_pause, "p")
    screen.onkey(game_resume, "Return")
    screen.listen()
    if running:
        if board == next_life_generation(board) == \
                next_life_generation(next_life_generation(board)) or all_zeroes(board):
            running = False
        else:
            show_good()
            screen.ontimer(show_good_2, t=0)
            # De waarde t hierboven stelt in hoeveel milliseconden er tussen
            # elke generatie van Life zijn. Gebruik een lage waarde (bv. 0 seconden, of 500
            # voor een halve seconde, enz.) om de beweging snel te laten zijn, of
            # een hoge waarde (bv. 1000 voor 1 seconde, 3000 voor 3 seconden, enz.)
            # voor langzamere bewegingen.


def game_pause():
    """Pauses the game"""
    global running
    running = False


def game_resume():
    """Resumes a paused game."""
    global running
    running = True
    show_good_2()


def blank():
    """Makes the board blank (resets the board)"""
    global board
    height = len(board)
    width = len(board[0])
    board = create_board(width, height)  # of zeros
    show(board)


def create_one_row(width):
    """ returns one row of zeros of width "width"...
         You might use this in your create_board(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row


def create_board(width, height):
    """ returns a 2d array of width and height """
    a = []
    for row in range(height):
        a += [create_one_row(width)]
    return a


def random_cells(width, height):
    """ Takes an empty board as input and modifies that board
        so that its inner cells (non-edge) are either 0 or 1
    """
    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            a[row][col] = choice([0, 1])

    return a
