def p56(l):
  tmp = 0
  for a in range(1,l):
    for b in range(1,l):
      #tmp = pow(a,b)
      #L = list(str(tmp))
      #print(l)
      #s = list(map(int,L))
      #print(s)
      #d = sum(s)
      #print(a,b,d)
      d = sum(map(int,list(str(a**b))))
      if d > tmp:
        tmp = d
        print(a,b,d)
  return tmp

print(p56(100))
