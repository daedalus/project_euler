
def p22():
  tmp = 0
  data = sorted(open("data/p022_names.txt",'r').readlines()[0].replace('"','').split(","))
  #print(data)
  pos = lambda a:ord(a)-64
  for i in range(0,len(data)):
    s = sum(list(map(pos,list(data[i]))))
    tmp += (s*(i+1))
    if data[i] == "COLIN":
      print(data[i],s,i+1)
  return tmp
 
print(p22())
