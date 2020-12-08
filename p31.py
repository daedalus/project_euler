
def p31(l):
  coins = [1,2,5,10,20,50,100,200]
  rcoins = coins[::-1][1::]
  tmp = 0
  i=0
  for b in range(0,(l//coins[6])+1):
    for c in range(0,(l//coins[5])+1):
      for d in range(0,(l//coins[4])+1):
        for e in range(0,(l//coins[3])+1):
          for f in range(0,(l//coins[2])+1):
           for g in range(0,(l//coins[1])+1):
             for h in range(0,(l//coins[0])+1):
               Z = list(zip(rcoins,[b,c,d,e,f,g,h]))
               s = sum(map(lambda x:x[0]*x[1],Z))
               print(i,tmp,Z,s)
               i+=1
               if s == l:
                 tmp+=1
               elif s > l:
                 break
  return tmp+1

print(p31(200))
