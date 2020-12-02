from lib import math

def p27(l):
  r = math.find_coeffs_for_equler_quadratic(l)
  return r[1] * r[2]

print(p27(1000))
