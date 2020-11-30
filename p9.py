from gmpy2 import *

def p9(n):
    tmp = 0
    for a in range(1,n):
        for b in range(1,n):
          aa, bb = a**2, b**2
          cc = aa + bb
          c = isqrt(cc)
          if c*c == cc:
              if a < b < c:
                  abc_sum = a + b + c
                  abc_mul = a * b * c
                  print(a, b, c, aa, bb, cc,abc_sum,abc_mul)
                  if abc_sum == n:
                      return abc_mul

print(p9(1000))
