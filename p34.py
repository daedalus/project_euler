from gmpy2 import *

def p34():
  tmp = 0
  n = 3
  while True:
    s = sum(list(map(fac,map(int,list(str(n))))))
    if s == n:
      tmp += s
      print(tmp)
    n+=1
p34()
