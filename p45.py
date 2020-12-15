from lib.math import triangular_number,pentagonal_number,hexagonal_number
import math

def p45_slow(i):
  c=0
  while i>0:
  #for i in range(1,I):
    for j in range(1,i):
      for k in range(1,j):
        T = triangular_number(i)
        P = pentagonal_number(j)
        H = hexagonal_number(k)
        print(c,i,j,k,T,P,H)
        if T == P == H:
          return T
        c+=1
    i+=1

#print(p45(55385))

def F(x):
  y = int((1.0 / 6) * (math.sqrt(12 * (x ** 2) + (12 * x) + 1) + 1)); 
  z = int((x + 1) / 2)
  T = triangular_number(x)
  P = pentagonal_number(y)
  H = hexagonal_number(z)
  if T == P == H:
      return T
  else:
      return False

def p45(i):
  f = False
  while f == False:
    f = F(i)
    print(i,f)
    if f != False:
      return f
    i+=1

print(p45(286))
