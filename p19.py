from functools import reduce
from gmpy2 import fac

def p19(n):
  return reduce(lambda a,b : a+b,list(map(int,list(str(fac(n))))))

print(p19(100))
