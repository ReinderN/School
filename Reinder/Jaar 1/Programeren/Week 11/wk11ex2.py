#
# wk11ex2.py
#
# namen: Reinder Noormans, Freek van Witzenburg en Bas Mellens
#
import random


def in_a_row_n_south(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading south and returns False otherwise.
    """
    h = len(a.data)
    w = len(a.data[0])
    if r_start < 0 or r_start + (n-1) > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a.data[r_start+i][c_start] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug


def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading northeast and returns False otherwise.
    """
    h = len(a.data)
    w = len(a.data[0])
    if r_start - (n-1) < 0 or r_start > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a.data[r_start-i][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug


def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading southeast and returns False otherwise.
    """
    h = len(a.data)
    w = len(a.data[0])
    if r_start < 0 or r_start + (n-1) > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a.data[r_start+i][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug


def in_a_row_n_east(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading east and returns False otherwise.
    """
    h = len(a.data)
    w = len(a.data[0])
    if r_start < 0 or r_start > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a.data[r_start][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug


class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We hoeven niets terug te geven vanuit een constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # de string om terug te geven
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # onderkant van het bord
        s += '\n'
        for x in range(0, self.width):
            s += ' ' + str(x % 10)

        # hier moeten de nummers nog onder gezet worden

        return s       # het bord is compleet, geef het terug

    def add_move(self, col, ox):
        '''deze functie voegt een steen(ox) toe in een collom(col)'''
        for row in range(0, self.height):
            if self.data[row][col] != ' ':
                self.data[row - 1][col] = ox
                return

        self.data[self.height - 1][col] = ox

    def clear(self):
        '''deze functie schoont het bord op'''
        self.__init__(self.width, self.height)

    def set_board(self, move_string):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.set_board('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.set_board('000000') to
           see them alternate in the left column.

           move_string must be a string of one-digit integers.
        """
        next_checker = 'X'   # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'

    def allows_move(self, col):
        '''deze functie controleerd of er eens steen in de collom(col) mag'''
        if col > self.width-1 or col < 0:
            return False
        if self.data[0][col] != ' ':
            return False
        return True

    def is_full(self):
        '''deze functie controleerd of het bord vol is'''
        full = 0
        for col in range(0, self.width):
            result = self.allows_move(col)
            if result is False:
                full += 1
        if full == self.width:
            return True
        return False

    def del_move(self, col):
        '''deze functie verwijdered de bovenste steen in een collom(col)'''
        for row in range(0, self.height):
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                return

    def wins_for(self, ox):
        """ wins_for code """
        # dit is pseudocode
        for row in range(0, self.height):
            for col in range(0, self.width):
                # controleer of je in één van de vier richtingen wint
                east_win = in_a_row_n_east(ox, row, col, self, 4)
                south_win = in_a_row_n_south(ox, row, col, self, 4)
                north_east_win = in_a_row_n_northeast(ox, row, col, self, 4)
                south_east_win = in_a_row_n_southeast(ox, row, col, self, 4)
                if east_win or south_win or north_east_win or south_east_win:
                    return True
        return False

    def cols_to_win(self, ox):
        '''controleerd de collomen die je kan vullen om te winnen'''
        L = []
        for row in range(0, 1):
            for col in range(0, self.width):
                if self.allows_move(col):
                    self.add_move(col, ox)
                    if self.wins_for(ox):
                        L += [col]
                    self.del_move(col)
        return L

    def ai_move(self, ox):
        '''berekent de beste zet die je kan doen om te winnen'''
        colLself = self.cols_to_win(ox)
        legal = []
        if ox == 'O':
            colLenemy = self.cols_to_win('X')
        else:
            colLenemy = self.cols_to_win('O')

        if colLself != []:
            legal += colLself
        elif colLenemy != []:
            legal += colLenemy
        else:
            L = [self.allows_move(x) for x in range(0, self.width)]
            for x, i in enumerate(L):
                if i:
                    legal += [x]
        return random.choice(legal)

    def host_game(self):
        '''Deze functie runt de hele vier op een rij game'''
        print('Welkom bij Vier op een rij!')
        volgende = 'X'
        AI = 'O'
        while True:
            print(self)
            if self.wins_for('X'):
                print('Gefeliciteerd, speler X heeft gewonnen!')
                break
            if self.wins_for('O'):
                print('Gefeliciteerd, speler O heeft gewonnen!')
                break
            if self.is_full():
                print('Het bord is vol en het is dus gelijkspel geworden.')
                break
            if volgende != AI:
                keuze = input('Keuze van ' + volgende + ': ')
                keuzeint = int(keuze)
            else:
                keuze = self.ai_move(volgende)
                keuzeint = int(keuze)
            if self.allows_move(keuzeint):
                self.add_move(keuzeint, volgende)
                if volgende == 'X':
                    volgende = 'O'
                else:
                    volgende = 'X'
            else:
                print('Deze zet is niet toegestaan.')


b = Board(7, 6)
b.set_board('0112232335')
assert b.cols_to_win('X') == [3]
assert b.cols_to_win('O') == [4]

assert b.ai_move('X') == 3
assert b.ai_move('O') == 4
