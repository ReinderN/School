#
# wk10ex1.py
#
# namen: Reinder Noormans, Freek van Witzenburg en Bas Mellens
#

# Eerst de klassedefinitie
# Hieronder definiëren we een aantal handige objecten van het type Date
#  +++ bewaar die en/of voeg je eigen toe! +++

class Date:
    """A user-defined data structure that
        stores and manipulates dates.
    """

    # de constructor heet altijd __init__ !
    def __init__(self, day, month, year):
        """Construct a Date with the given day, month, and year."""
        self.day = day
        self.month = month
        self.year = year

    # de "afdruk"-functie heet altijd __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
            object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
            it more often is used implicitly via the print statement
            or simply by expressing self's value.
        """
        s = "{:02d}-{:02d}-{:04d}".format(self.day, self.month, self.year)
        return s

    # Hier is een voorbeeld van een "methode" van de klasse Date:
    def is_leap_year(self):
        """Returns True if the calling object is
        in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """Returns a new object with the same day, month, year
        as the calling object (self)."""
        dnew = Date(self.day, self.month, self.year)
        return dnew

    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
            in history as ==.  This way, we don't need to use the awkward
            d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def is_before(self, d2):
        '''This function returns True if date is befores another date'''
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __lt__(self, d2):
        '''This function changes the way > behaves'''
        return self.is_before(d2)

    def is_after(self, d2):
        '''This function returns True if date is after another date'''
        if self < d2:
            return False
        else:
            return True

    def __gt__(self, d2):
        '''This function changes the way < behaves'''
        return self.is_after(d2)

    def tomorrow(self):
        '''This function changes self to the day after self'''
        if self.month in [1, 3, 5, 7, 8, 10] and self.day == 31:
            self.day = 0
            self.month += 1
        elif self.month in [4, 6, 9, 11] and self.day == 30:
            self.day = 0
            self.month += 1
        elif self.month == 2:
            if self.is_leap_year() and self.day == 29:
                self.day = 0
                self.month += 1
            elif (self.is_leap_year() is False) and self.day == 28:
                self.day = 0
                self.month += 1
        elif self.month == 12 and self.day == 31:
            self.day = 0
            self.month = 1
            self.year += 1
        self.day += 1

    def yesterday(self):
        '''This function changes self to the day before self'''
        if self.month in [5, 7, 10, 12] and self.day == 1:
            self.day = 31
            self.month -= 1
        elif self.month in [2, 4, 6, 8, 9, 11] and self.day == 1:
            self.day = 32
            self.month -= 1
        elif self.month == 3:
            if self.is_leap_year() and self.day == 1:
                self.day = 30
                self.month -= 1
            elif (self.is_leap_year() is False) and self.day == 1:
                self.day = 29
                self.month -= 1
        elif self.month == 1 and self.day == 1:
            self.day = 32
            self.month = 12
            self.year -= 1
        self.day -= 1

    def add_n_days(self, n):
        '''this function adds n days'''
        for x in range(n):
            self.tomorrow()
            print(self)

    def sub_n_days(self, n):
        '''This function subtracts n days'''
        for x in range(n):
            self.yesterday()
            print(self)

    def __iadd__(self, n):
        '''The add equals funtion +='''
        self.add_n_days(n)
        return self

    def __isub__(self, n):
        '''the subtract equals function -='''
        self.sub_n_days(n)
        return self

    def diff(self, d2):
        '''Calculates the difference between self and d2'''
        self_copypos = self.copy()
        self_copyneg = self.copy()
        rotation = 0
        while self_copypos.is_before(d2) or self_copyneg.is_after(d2):
            self_copyneg.yesterday()
            self_copypos.tomorrow()
            rotation += 1
        if self_copypos == d2:
            rotation *= -1
        else:
            rotation -= 1
        return rotation

    def __sub__(self, d2):
        '''the subtract - function'''
        return self.diff(d2)

    def dow(self):
        '''Prints the day of the week the date is at'''
        count = 0
        d0 = Date(0, 0, 0)
        while self.is_after(d0):
            self.yesterday()
            count += 1
        dow = (count % 7)-1
        if dow == 1:
            return 'monday'
        elif dow == 2:
            return 'Tuesday'
        elif dow == 3:
            return 'Wednesday'
        elif dow == 4:
            return 'Thursday'
        elif dow == 5:
            return 'Friday'
        elif dow == 6:
            return 'Saturday'
        elif dow == 0:
            return 'Sunday'

    #
    # vergeet niet je code voor de klasse Date HIERBOVEN toe te voegen; in de klassedefinitie
    #
    #
    # een aantal datums om mee te werken...
    #
    # Het handige van ze hier plaatsen is dat ze elke keer dat de software uitgevoerd
    #   wordt ze opnieuw gedefinieerd worden (en dat is nodig om te testen!)
    #
d = Date(7, 12, 1941)    # Vandaag?
d2 = Date(21, 12, 2020)   # Kerstvakantie
ny = Date(1, 1, 2021)   # Nieuwjaar
nd = Date(1, 1, 2030)   # Nieuw decennium
nc = Date(1, 1, 2100)   # Nieuwe eeuw
graduation = Date(12, 7, 2024)   # Pas dit zelf aan!
vacation = Date(19, 7, 2021)     # Dit ook ~ zomervakantie!
sm1 = Date(28, 10, 1929)    # Krach aandelenbeurs
# Nog een beurskrach: Maandagen in okt. zijn gevaarlijk...
sm2 = Date(19, 10, 1987)

x = d.dow()

print(x)
