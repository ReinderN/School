# count_evens uit List-2
def count_evens(nums):
    total = 0
    for x in nums:
        if x % 2 == 0:
            total += 1
    return total

# sum13 uit List-2


def sum13(nums):
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
    dblchr = ''
    for x in str:
        dblchr += x + x
    return dblchr
