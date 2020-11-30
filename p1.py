def p1(n):
  tmp=0
  for i in range(1,n):
    if i % 3 == 0 or i % 5 == 0:
      tmp+=i
  return tmp

print(p1(10))
print(p1(1000))

