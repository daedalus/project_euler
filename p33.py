def p33():
  tmp = []
  for i in range(1,100):
    for j in range(1,100):
      a = str(i)
      b = str(j) 
      if len(a) == 2 and len(b) == 2:
        c = float(i)/j 
        if c <= 1.0:
          if ( a[0] != a[1]) and (a[1] == b[0] and int(b[1])>0) == True:
            c2 = (float(int(a[0]))/int(b[1]))
            if abs(c2-c) == 0:
              tmp.append((i,j))
  print(tmp)
  nom=1
  den=1
  for f in tmp:
    nom *= f[0]
    den *= f[1]
  print(nom,den,float(nom)/den)
  return max(nom,den)//min(nom,den)

print(p33())
