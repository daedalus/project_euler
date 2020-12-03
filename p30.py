from lib.math import num_to_digits


def find_digit_powers(p):
  i=0
  tmp = []
  while i <= 10**(p+1):  
    s = 0
    digits = num_to_digits(i)
    for d in digits:
      s += (d**p)
    if i > 1 and (s == i):
      tmp.append(i)
    i+=1
  return tmp


def p30(a):
  return sum(find_digit_powers(a))  

print(p30(4))
print(p30(5))

