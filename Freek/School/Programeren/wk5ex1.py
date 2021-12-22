# Programmeren I, Practicum 5
# Bestandsnaam: wk5ex1.py
# Naam: Freek van Witzenburg
# Probleemomschrijving: conversie binair <-> decimaal

# Functie is_odd(n) ->
def is_odd(n):
    """is_odd(n) checks integer n and gives back True or False.
    if the integer is even, odd will return False.
    if the integer is uneven, odd will return True.
      """
    if n % 2 != 0:

      return  True
    else:
      return False
if is_odd(42) is not False:
    raise AssertionError
if is_odd(43) is not True:
    raise AssertionError
if is_odd(44) is not False:
    raise AssertionError
  # Functie num_to_binary(n) ->

def num_to_binary(n):
   """num_to_binary replaces a integer with a binary number.
  if the modulo of n is equal to 1 it returns a 1.
  if the modulo of n is equal to 0 it returns a 0.
  """
   if n == 0:
     return ""
   elif n % 2 == 1:
     return num_to_binary(n // 2) + "1"
   else:
     return num_to_binary(n // 2) + "0"
if num_to_binary(0) != "":
    raise AssertionError
if num_to_binary(42) != "101010":
    raise AssertionError
if num_to_binary(5) != '101':
    raise AssertionError
if num_to_binary(12) != '1100':
    raise AssertionError
  # functie binary_to_num(s) ->
def binary_to_num(s):
   """binary_to_num changes a binary number to a integer.
  input s is a binary number.
  """
   if s == "":
      return 0
  # als het laatste cijfer een '1' is...
   elif s[-1] == "1":
      return 2*binary_to_num(s[:-1]) + 1
   else: # laatste cijfer moet een '0' zijn
     return 2*binary_to_num(s[:-1]) + 0
if binary_to_num('') != 0:
    raise AssertionError
if binary_to_num("101") != 5:
    raise AssertionError
if binary_to_num("101010") != 42:
    raise AssertionError
if binary_to_num("100") != 4:
    raise AssertionError
  # Functie increment(s) ->
def increment(s):
   """increment accepts a binairy string with 0's and 1's
  and gives back a base number 2.
  """
   if (s == '11111111'):
     return('0'*8)
   n = binary_to_num(s)
   x = n + 1
   y = num_to_binary(x)
   len_y = len(y)
   return ('0'* (8-len_y)) + y
if increment("00000000") != '00000001':
    raise AssertionError
if increment("00000001") != '00000010':
    raise AssertionError
if increment("00000111") != '00001000':
    raise AssertionError
if increment("11111111") != '00000000':
    raise AssertionError
  # Functie count(s, n) ->
def count(s, n):
   """count accepts a binairy string and muliplies is n times from start
  position s.
  count uses function increment.
  every stap is displayed.
  """
   if n < 0:
    return
   else:
    print(s)
    count(increment(s), n-1)
  # geen asserts mogelijk aangezien count niets returnt.
  # Functie num_to_ternary(n) ->
def num_to_ternary(n):
   """Converts number to ternary string.
  """
   if n == 0:
    return ""
   elif n % 3 == 1:
    return num_to_ternary(n // 3) + "1"
   elif n % 3 == 2:
    return num_to_ternary(n // 3) + "2"
   else:
    return num_to_ternary(n // 3) + "0"
if num_to_ternary(42) != '1120':
    raise AssertionError
if num_to_ternary(4242) != '12211010':
    raise AssertionError
if num_to_ternary(0) != '':
    raise AssertionError
  # Functie ternary_to_num(s) ->
def ternary_to_num(s):
   """binary_to_num changes a binary number to a integer.
  input s is a binary number.
  """
   if s == "":
    return 0
  # als het laatste cijfer een '1' is...
   elif s[-1] == "2":
    return 3*ternary_to_num(s[:-1]) + 2
   elif s[-1] == "1":
    return 3*ternary_to_num(s[:-1]) + 1
   else: # laatste cijfer moet een '0' zijn
    return 3*ternary_to_num(s[:-1]) + 0
if ternary_to_num("1120") != 42:
    raise AssertionError
if ternary_to_num("12211010") != 4242:
    raise AssertionError
if ternary_to_num("10") != 3:
    raise AssertionError
  # Functie balanced_ternary_to_num(s) ->
def balanced_ternary_to_num(s):
   """returns a decimal value equal to balanced ternary string s.
  """
   if s == "":
    return 0
   elif s[-1] == "-":
    return 3 * balanced_ternary_to_num(s[:-1]) - 1
   elif s[-1] == "+":
    return 3 * balanced_ternary_to_num(s[:-1]) + 1
   elif s[-1] == "0":
    return 3 * balanced_ternary_to_num(s[:-1]) + 0
if balanced_ternary_to_num("+---0") != 42:
    raise AssertionError
if balanced_ternary_to_num("++-0+") != 100:
    raise AssertionError
if balanced_ternary_to_num("+0--0") != 69:
    raise AssertionError
  # Functie num_to_balanced_ternary(n) ->
def num_to_balanced_ternary(n):
   """returns a balanced ternary string that is equal to value n.
  """
   if n == 0:
    return ''
   elif n % 3 == 0:
    return num_to_balanced_ternary(n // 3) + '0'
   elif n % 3 == 1:
    return num_to_balanced_ternary(n // 3) + '+'
   elif n % 3 == 2:
    return num_to_balanced_ternary((n // 3) + 1) + '-'
if num_to_balanced_ternary(42) != '+---0':
    raise AssertionError
if num_to_balanced_ternary(100) != '++-0+':
    raise AssertionError
if num_to_balanced_ternary(69) != '+0--0':
    raise AssertionError

