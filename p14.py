def rule(n):
  if n % 2 == 0:
    return (n//2)
  else:
    return (3*n)+1

def count_chain(ub):
  tmp = ub
  num=1
  while tmp > 1:
    tmp = rule(tmp)
    num += 1
  return num

def p14(ub):
  tmp = 0
  r = 0
  for i in range(ub,0,-1):
    c = count_chain(i)
    print(i,c)
    if c > tmp:
      tmp = c
      r = i
  return r

print(p14(10**6))
