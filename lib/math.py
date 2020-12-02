from gmpy2 import is_prime
from functools import reduce


def prime_sieve(l):
  primes = [2]
  p = 2
  while len(primes) <= l:
    f = True
    p += 1
    for x in primes:
      if p % x == 0:
        f = False
        break
    if f == True:
      primes.append(p)
  return primes


def is_palindrome(n):
  s = str(n)
  return s == s[::-1]


def count_proper_divisors_fast_plus_num(num):
  i = 2
  k = 2
  while i <= num//i:
     if num % i == 0:
       k += 2
     i += 1
  return k


def proper_divisors(n):
  tmp = []
  for i in range(2,n+1):
    if n % i == 0:
      tmp.append(n//i)
  return tmp


def list_sum(lst):
  return reduce(lambda a,b : a+b,lst)


def list_prod(lst):
    return reduce((lambda x, y: x * y), lst)


def aliquot_sum(n):
   if n == 1:
     return 0
   elif n == 2:
     return 1
   elif n > 2:
     return list_sum(proper_divisors(n))


def is_amicable(n):
  a = aliquot_sum(n)
  b = aliquot_sum(a)
  return (n == b != a)


def is_perfect_number(n):
  return aliquot_sum(n) == n


def is_abundant_number(n):
  return aliquot_sum(n) > n
