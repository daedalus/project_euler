from gmpy2 import is_prime
from functools import reduce
from itertools import product

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


def cartesian_product(a,b):
  return list(product(a,b))


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


def is_deficient_number(n):
  return aliquot_sum(n) < n


def num_to_digits(n):
  return list(map(int,list(str(n))))


def fib(n):
  a = 0
  b = 1 
  for i in range(0,n):
    c = b + a
    a = b
    b = c
  return a


def find_coeffs_for_equler_quadratic(l):
  max_n = 0
  max_a = 0
  max_b = 0
  for a in range(-l,l):
    for b in range(-l,l):
      c = True
      n=-1
      while c:
        n += 1
        fx = n**2 + a*n + b
        c = is_prime(fx)
        if n > max_n:
          max_n = n
          max_a = a
          max_b = b
    print(max_n,max_a,max_b)

  return max_n,max_a,max_b


def champernowne_constant_digits(g):
  return [int(d) for n in range(g) for d in str(n)]

