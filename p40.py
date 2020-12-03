from lib.math import champernowne_constant_digits
import math

def p40(l):
  tmp = 1
  max_dig = int(math.log(l,10))
  lst = champernowne_constant_digits(l)
  for i in range(0,max_dig+1):
    d = lst[10**i]
    tmp*=d
    print(i,10**i,d)

  return tmp

print(p40(10**5))
