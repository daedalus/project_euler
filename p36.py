from lib.math import is_palindrome

def p36(n):
  s = 0
  while n > 0:
    a = is_palindrome(n)
    b = str(bin(n)).replace("0b","")
    c = is_palindrome(b)
    if a == c == True:
      print(n,a,b,c)
      s += n
    n-=1
  return s

print(p36(10**6))
