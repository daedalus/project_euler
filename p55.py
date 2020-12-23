from lib.math import is_palindrome, is_lychrel_number

def p55(L):
  c = 0
  for i in range(0,L):
    if is_lychrel_number(i,l=50) == False:
      print(i,c)
      c += 1
  return c

print(p55(10**4))
