from gmpy2 import *

def p5(n):
    if n > 1:
    	return lcm(n,p5(n-1))
    else:
        return 1
    

print(p5(20))
