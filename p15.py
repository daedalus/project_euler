from gmpy2 import *

def p15(n): 
  return fac(2*n)/(fac(n)**2) # https://en.wikipedia.org/wiki/Central_binomial_coefficient

print(p15(2))
print(p15(4))
print(p15(20))

