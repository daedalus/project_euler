# https://en.wikipedia.org/wiki/Amicable_numbers

from gmpy2 import is_prime
from functools import reduce

def prop_div(n):
  tmp = []
  for i in range(2,n+1):
    if n % i == 0:
      tmp.append(n//i)
  return tmp

def list_sum(lst):
  return reduce(lambda a,b : a+b,lst)

def aliquot_sum(n):
   if n == 1:
     return 0
   elif n == 2:
     return 1
   elif n > 2:
     d0 = prop_div(n)
     a = list_sum(d0)
     return a

def is_amicable(n):
  #print(n)
  r = False
  a = aliquot_sum(n)
  b = aliquot_sum(a)
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

if __name__ == "__main__":
  print(p21(10**4))


