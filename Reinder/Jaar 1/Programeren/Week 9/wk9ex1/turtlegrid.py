from turtle import *

current_L = None

col = -1
row = -1

current_xs = []
current_ys = []


def get_pos(mouse_x, mouse_y):
    """Returns the row and column clicked by the mouse in a tuple."""
    global current_xs
    global current_ys
    global col
    global row

    col = 0
    row = 0

    for i in range(len(current_xs) - 1):
        if current_xs[i] <= mouse_x < current_xs[i + 1]:
            col = i
    for i in range(len(current_ys) - 1):
        if current_ys[i] <= mouse_y < current_ys[i - 1]:
            row = i - 1

    if mouse_x > 0 and col == 0:
        col = len(current_xs) - 2
    if mouse_y < 0 and row == 0:
        row = len(current_ys) - 2

    return (row, col)


clr_d = {0: "white", 1: "red", 2: "blue", 3: "green", 4: "gold"}


def set_color(key, color):
    global clr_d
    clr_d[key] = color
    return


def color_lookup(clr):
    global clr_d
    if clr in clr_d:
        return clr_d[clr]
    else:
        return clr


def drawsq(ulx, uly, side, clr):
    """Draws a single square, and fills it based on the
        number held in that square's position on the array"""
    delay(0)
    tracer(False)
    up()
    # stel de kleur in
    pencolor("black")
    # zoek de kleur op
    clr = color_lookup(clr)
    # tekenen!
    try:
        fillcolor(clr)
    except:
        print("Color", clr, "was not recognized.")
        print("Using blue instead.")
        fillcolor("blue")

    goto(ulx, uly)
    down()
    seth(0)  # ga naar rechts

    begin_fill()
    for s in range(4):
        forward(side)
        right(90)
    end_fill()

    up()


def show_1d(l):
    """Shows a 1d list l using turtle graphics """
    # deze waarde onthouden!
    global current_L
    current_L = l

    w = window_width()
    h = window_height()
    if len(l) == 0:
        print("You can't show(l) when l is empty.")
        return

    n = len(l) + 2  # 2 extra voor marge aan de zijkant

    sq_side = min(w / float(n), h / float(3), 100.0)

    uly = 0 + sq_side / 2.0
    ulx = -sq_side * len(l) / 2.0

    global current_ys
    current_ys = [-uly, uly]
    global current_xs
    current_xs = [ulx]

    clear()
    for clr in l:
        drawsq(ulx, uly, sq_side, clr)
        ulx += sq_side
        current_xs.append(ulx)

    return


def show_2d(l):
    """Shows a 2d grid l using turtle graphics"""
    # dit onthouden!
    global current_L
    current_L = l

    w = window_width()
    h = window_height()
    if len(l) == 0:
        print("You can't show(l) when l is empty.")
        return

    n = len(l) + 2  # 2 extra voor marge aan de zijkant

    sq_side = min(w / float(n), h / float(n), 100.0)

    uly = 0 + sq_side * len(l) / 2.0
    ulx = -sq_side * len(l[0]) / 2.0

    global current_ys
    current_ys = [uly]
    global current_xs
    current_xs = [ulx]

    clear()
    for row in l:
        for clr in row:
            drawsq(ulx, uly, sq_side, clr)
            ulx += sq_side
            if ulx not in current_xs:
                current_xs.append(ulx)
        uly -= sq_side
        current_ys.append(uly)
        ulx = -sq_side * len(l) / 2.0
    return


def show(l):
    """Shows the list or grid l using the graphics"""
    if type(l[0]) == list:
        show_2d(l)
    else:
        show_1d(l)
    return


# stel de muishandler in...
def life_mouse_handler(x, y):
    """ This function is called with each mouse click.

        Its inputs are the pixel location of the
        next mouse click: (x,y)

        It computes the column and row (within the board)
        where the click occurred with get_pos, and changes the
        color of the clicked square.

        The overall list is shared between turtle graphics
        and the other parts of your program as a global
        variable named current_L. In general, global variables
        make software more complex, but sometimes they are
        necessary.
    """
    get_pos(x, y)  # werk de positie bij
    if row == 0 or row == len(current_L) - 1 or col == 0 or col == len(current_L[0]) - 1:
        print("Don't click on the border!!! >:O")
    else:
        current_L[row][col] = 1 - current_L[row][col]
    show(current_L)
