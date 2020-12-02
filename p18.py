
t = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")

def T(t):
  i=0
  R=[]
  for r in t:
    r = list(map(int,r.split(" ")))
    R.append(r) 
  return R

t = T(t)

def p18(t,s=0,l=0):
  #print("p18",t)
  print("p18",l,s)
  A=[]
  B=[]
  i=0
  s1 =s
  s2 =s
  if len(t) == 1:
    #s = t[0][0]
    return t[0][0]
    #s = t[0][0] 
  else:
    for i in range(0,len(t)):
      #print(r)
      if i == 0:
        s1 = t[0][0]
        s2 = s1
      else:
        A.append(t[i][1:])
        B.append(t[i][:-1])
      i+=1
  s1 += p18(A,s=s1,l=l+1)
  s2 += p18(B,s=s2,l=l+1)
  #print(s1)
  #print(s2) 
  if s1 > s2:
    return s1
  else :
    return s2
   
if __name__ == "__main__":
  print(p18(t))
