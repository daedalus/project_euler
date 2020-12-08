from itertools import permutations  

def p31(l):
  coins = [1,2,5,10,20,50,100,200]
  #f = list(map(lambda x: 200//x, coins))
  for perm in permutations(coins):
    m = l
    tmp = []
    for c in perm:
      m = m // c
      #print(m)
      tmp.append(m)
      if m == 0:
        break
      print(tmp)
  #print(f)
  #return c

p31(200)
