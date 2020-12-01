from gmpy2 import *

def p12(l):
    tmp = 0
    n=0
    while True:
       n+=1 
       tmp+=n
       dc=0
       for d in range(1,tmp//2):
            if tmp % d == 0:
               dc += 2
            if dc >= l:
               break 
       print(n,tmp,dc)
    return tmp

print(p12(500))
