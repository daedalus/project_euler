from lib.strings import xor_codec

def p56():
  with open("data/p059_cipher.txt") as fp:
    data = list(map(int,fp.read().split(",")))
  lt = 0
  for A in range(97,123):
    for B in range(97,123):
      for C in range(97,123):
        key = [A,B,C]
        tmp = xor_codec(data,key)
        l=0
        #print(tmp)
        for t in tmp:
          if 122 >= t >= 65:
            l+=1
        #l = len(tmp.split())
        if l > lt:
          lt = l
          K = key
          D = tmp
          #print(K,l,str(map(ord,tmp[0:10])),str(map(ord(tmp[::-1][0:10][::-1]))))
          print(K,l,"".join(list(map(chr,D)))[0:10])
  return sum(D)

print(p56())
#print(dec(data,K))

