#https://oeis.org/A001913
from gmpy2 import next_prime
from lib.math import cycleLength

def max_cyclefind(l)
  d = None
  tmp = 0
  p = 6
  primes = [3] # exclude [2,5] beacuse coprimes of 10.
  while p <= l:
    p = next_prime(p)
    primes.append(p)
  for p in primes:
    c = cycleLength(1,p)
    if c > tmp:
      tmp = c
      d = p
   print(p,c)
  return d

def p26(l)
  return max_cyclefind(l)

print(p26(1000))

