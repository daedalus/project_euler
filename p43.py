from lib.math import is_pandigital
from itertools import permutations

def f(i):
  d = list(str(i))
  tmp = int(d[1]+d[2]+d[3]) % 2
  tmp += int(d[2]+d[3]+d[4]) % 3
  tmp += int(d[3]+d[4]+d[5]) % 5
  tmp += int(d[4]+d[5]+d[6]) % 7
  tmp += int(d[5]+d[6]+d[7]) % 11
  tmp += int(d[6]+d[7]+d[8]) % 13
  tmp += int(d[7]+d[8]+d[9]) % 17
  if (tmp == 0):
    return int(i)
  else:
    return 0

def p43():
  return sum(map(lambda x:f("".join(x)),permutations("0123456789")))

print(p43())
