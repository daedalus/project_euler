from gmpy2 import gcd

def p182(p,q):
  phi = (p-1)*(q-1)
  return sum([e for e in range(2,phi) if gcd(e,phi) == 1 and (gcd(e-1,p-1)+1)*(gcd(e-1,q-1)+1) == 9])

print(p182(1009,3643))
