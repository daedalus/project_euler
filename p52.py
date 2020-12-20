def P(n):
  f = True
  tmp = []
  s1 = "".join(sorted(str(n)))
  for i in range(2,7):
    s2 = "".join(sorted(str(n*i))) 
    if s1 != s2:
      f = False
      break
  return f

def p52(n=2):
  f = False
  while f == False:
   f = P(n)
   n += 1
  return n-1

print(p52())
