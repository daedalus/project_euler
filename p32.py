from lib.math import is_pandigital

def p32():
  tmp = []
  for i in range(0,9999):
    for j in range(0,i+1):
      M = i * j
      sM=str(M)
      sI=str(i)
      sJ=str(j)
      #print(M,i,j)
      if is_pandigital(sM+sI+sJ)==True:
        print(i,j,M)
        if M not in tmp:
          tmp.append(M)
  return sum(tmp)


print(p32())
