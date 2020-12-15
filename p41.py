from gmpy2 import is_prime
from lib.math import is_pandigital
from itertools import permutations

def p41_slow(l):
  N = (10**l)+1
  while N > 1:
    a = is_prime(N)
    b = is_pandigital(N,n=l)
    print(N,a,b)
    if a == b == True:
      return N
    N-=2
 
def p41(l):
  tmp = []
  while l > 3:
    i = list(map(str,range(1,l+1)))
    for N in map(lambda x:int("".join(list(x))), permutations(i)):
      a = is_prime(N)
      if a == True:
        tmp.append(N)
    l-=1
  return sorted(tmp)[-1]

print(p41(9))
#print(p41(9))
