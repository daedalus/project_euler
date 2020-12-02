from lib import math

def p25(l):
   n=0
   while True:
     n+=1
     f = math.fib(n)
     if len(str(f)) == l:
       break
   return n

print(p25(1000))
