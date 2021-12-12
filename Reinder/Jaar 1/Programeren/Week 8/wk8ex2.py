# Bestandsnaam: wk8ex2.py
# Naam: Bas Mallens, Reinder Noormans, Freek van Witzenburg

# count_evens uit List-2
def count_evens(nums):
    """Geeft alle even getallen terug uit list-2"""
    total = 0
    for x in nums:
        if x % 2 == 0:
            total += 1
    return total

# sum13 uit List-2


def sum13(nums):
    """" Telt alle getallen uit list 2. """
    sum = 0
    next = False
    for x in nums:
        if next == False:
            if x == 13:
                sum += 0
                next = True
            else:
                sum += x
        else:
            next = False
    return sum

# big_diff uit List-2


def big_diff(nums):
    """Geeft de grootste veschril tussen 2 getallen terug uit list 2. """
    biggest = 0
    smallest = 999999
    for x in nums:
        if x < smallest:
            smallest = x
        if x > biggest:
            biggest = x
    difference = biggest - smallest
    return difference

# sum67 uit List-2


def sum67(nums):
    """Geeft alle getallen uit list 2 weer."""
    sum = 0
    geweest = False
    for x in nums:
        if geweest == False:
            if x == 6:
                geweest = True
            else:
                sum += x
        else:
            if x == 7:
                geweest = False
    return sum

# centered_average uit list-2


def centered_average(nums):
    """Geeft een mediaan van de getallen uit list 2 weer."""
    biggest = 0
    smallest = 999999
    for x in nums:
        if x < smallest:
            smallest = x
        if x > biggest:
            biggest = x
    cave = (sum(nums)-biggest-smallest) // (len(nums)-2)
    return cave

# has22 uit list-2


def has22(nums):
    """Bij een lijst waar 2x een 2 achter elkaar zit zal de functie true geven. Bij een lijst waar dat niet voorkomt false."""
    last = 0
    two2 = False
    for x in nums:
        if last == 2 and x == 2:
            two2 = True
        else:
            last = x
    return two2

# double_char uit String-2


def double_char(str):
    """Verdubbelt elke letter uit een string"""
    dblchr = ''
    for x in str:
        dblchr += x + x
    return dblchr


assert count_evens([4, 123, 2132, 345, 456]) == 3
assert count_evens([2314, 234, 456, 1235, 332, 436]) == 5
assert count_evens([196, 27634, 5433, 345, 1843, 324]) == 3

assert sum13([4, 123, 2132, 345, 456]) == 3060
assert sum13([2314, 234, 456, 1235, 332, 436]) == 5007
assert sum13([196, 27634, 5433, 345, 1843, 324]) == 35775

assert big_diff([4, 123, 2132, 345, 456]) == 2128
assert big_diff([2314, 234, 456, 1235, 332, 436]) == 2080
assert big_diff([196, 27634, 5433, 345, 1843, 324]) == 27438

assert sum67([4, 123, 2132, 345, 456]) == 3060
assert sum67([2314, 234, 456, 1235, 332, 436]) == 5007
assert sum67([196, 27634, 5433, 345, 1843, 324]) == 35775

assert centered_average([4, 123, 2132, 345, 456]) == 308
assert centered_average([2314, 234, 456, 1235, 332, 436]) == 614
assert centered_average([196, 27634, 5433, 345, 1843, 324]) == 1986

assert has22([4, 123, 2132, 345, 456]) == False
assert has22([2314, 2, 2, 1235, 22, 436]) == True
assert has22([196, 27634, 5433, 345, 1843, 324]) == False

assert double_char('abc') == 'aabbcc'
assert double_char('AaBbCc') == 'AAaaBBbbCCcc'
assert double_char('Bas Stinkt') == 'BBaass  SSttiinnkktt'
