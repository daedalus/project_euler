from gmpy2 import is_prime
from lib.math import is_truncatable_prime

def p37(l):
  n = 0
  s = 0
  c = 0
  while True:
    if n > 7 and is_prime(n) == True:
      if is_truncatable_prime(n) == True:
        print(c,n)
        s += n
        c += 1
        if c == l:
          return s
    n+=1

print(p37(11))
