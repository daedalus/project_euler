from lib.math import is_pandigital

def cp(N,l):
  l = list(range(1,l+1))
  x = "".join(list(map(lambda x:str(x*N),l)))
  return x

def p38(l):
  n = 0
  tmp = []
  while n<=10**l:
    for i in range(1,10):
      N = cp(n,i)
      if len(N) == 9:
        a = is_pandigital(N)
        #print(n,i,N,a)
        if a == True:
          print(n,i,N,a)
          tmp.append(int(N))
          break
      #else:
      #  break
    n+=1
  return sorted(tmp)[-1]


print(p38(4))
#print(is_pandigital(192384576))
