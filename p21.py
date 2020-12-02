# https://en.wikipedia.org/wiki/Amicable_numbers

from gmpy2 import is_prime
from functools import reduce

def prop_div(n):
  tmp = []
  for i in range(2,n+1):
    if n % i == 0:
      tmp.append(n//i)
  return tmp

def is_amicable(n):
  #print(n)
  r = False
  d0 = prop_div(n)
  a = None
  b = None
  if len(d0) > 0:
    a = reduce(lambda a,b : a+b,d0)
    print(d0,a)
    d1 = prop_div(a)
    if len(d1) > 0:
      b = reduce(lambda a,b : a+b,d1)
      print(d1,b)
      r = (n == b != a)
  print(n,a,b,n==a,n==b)
  return r

def p21(l):
  tmp=0
  for i in range(1,l):
    if is_prime(i) == False:
      if is_amicable(i) == True:
        print(i)
        tmp += i
  return tmp


def test():
  print(is_amicable(220))
  print(is_amicable(284))
  print(is_amicable(2))
  print(is_amicable(1))
  print(is_amicable(1184))
  print(is_amicable(1210))
  print(is_amicable(9363584))
  print(is_amicable(9437056))
  print(is_amicable(496))
  print(is_amicable(8128))


print(p21(10**4))


