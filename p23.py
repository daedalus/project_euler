# https://en.wikipedia.org/wiki/Perfect_number
# https://en.wikipedia.org/wiki/Abundant_number
# https://en.wikipedia.org/wiki/Deficient_number

from gmpy2 import is_prime
from functools import reduce
from p21 import *
from itertools import product

def is_perfect_number(n):
  return aliquot_sum(n) == n

def is_abundant_number(n):
  return aliquot_sum(n) > n

def p23(l):
  tmp = []
  sums = [0] * (l+1)
  s = 0
  for i in range(1,l+1):
    if is_abundant_number(i) == True:
       #print("%d %s\r" % (i,is_))
       tmp.append(i)
  for i in tmp:
    for j in tmp:
      t = i + j 
      if t <= l:
        print(i,j,t)
        if sums[t] == 0:
          sums[t] = t
  for i in range(1,len(sums)):
     if sums[i] == 0:
       s += i
       print(i,s)

  return s
  #print(list(map(sum,zip(tmp,tmp))))
  #L = list(set(map(sum,list(product(tmp,tmp)))))
  #return list_sum(L) 

if __name__ == "__main__":
  print(p23(28123))
  #print(p23(2000))

