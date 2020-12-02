from functools import reduce
from lib import math

def p26(l):
  a = [x for x in range(2,l+1)]
  b = math.cartesian_product(a,a)
  return len(set(list(map(lambda x: x[0] ** x[1], b))))

print(p26(100))

