from lib.math import pentagonal_number
import math

def F(x,y):
  z1 = int((1.0 / 6) * (math.sqrt(36 * (x ** 2) - (12 * x) + 36 * (y ** 2) + (0  * y) + 1) + 1)) 
  z2 = int((1.0 / 6) * (math.sqrt(36 * (x ** 2) - (12 * x) - 36 * (y ** 2) + (12 * y) + 1) + 1))
  return z1,z2

def p44(x):
  #y = 1
  c=0
  while x>0:
  #for y in range(1,20):
    for y in range(1,x):
      s,d = F(x,y)
      S = pentagonal_number(s)
      D = pentagonal_number(d)
      X = pentagonal_number(x) 
      Y = pentagonal_number(y)
      print(c,(x,y,s,d),(X,Y,S,D))
      if D == X - Y and S == X + Y:
        return D
      #if D > 1:
      #  return D
      c+=1
    x+=1

print(p44(1))
#print(F(4,7))
