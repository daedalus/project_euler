from gmpy2 import is_prime
from lib/strings import string_rot_cycle

def p35(l):
  tmp = 0
  n=0
  c = 0 
  while n<=l:
    sn = str(n)
    if is_prime(n):
      L = list(map(lambda a:is_prime(int(a)),string_rot_cycle(sn)))
      if all(x == True for x in L):
        print(n,c)
        c+=1
    n+=1
  return c

print(p35(10**6))
