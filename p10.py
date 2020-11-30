from gmpy2 import *

l=2*(10**6)

def p10(n):
    p = 2
    tmp = 2
    while True:
        p = next_prime(p)
        if p <= n:
            tmp += p
        else:
            break
        print(p,tmp)
    return tmp

print(p10(l))

