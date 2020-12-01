def p16(n):
  return sum(list(map(int,list(str(2**n)))))
  
print(p16(15))
print(p16(1000))

