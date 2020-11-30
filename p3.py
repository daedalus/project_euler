from gmpy2 import *

def pollard_rho(n, seed=2, p=2, mode=1):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5
    if is_prime(n):
        return n
    if mode == 1:
        f = lambda x: x ** p + 1
    else:
        f = lambda x: x ** p - 1
    x, y, d = seed, seed, 1
    while d == 1:
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd((x - y) % n, n)
    return None if d == n else d

def p3(n):
	tmp = n
	tmp2 = []
	tmp3 = 1
	while tmp > 1:
		f = pollard_rho(n//tmp3)
		tmp3 *= f
		tmp2 += [f]
		tmp//=f
	return tmp2

print(p3(600851475143))
