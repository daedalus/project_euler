from lib.math import triangular_number as T

def word_value(word):
  v = 0
  for l in word:
    v += (ord(l)-96)
  return v

def p42():
  twords = list(map(T,range(35)))
  fp = open("data/p042_words.txt","r")
  words = fp.readline().replace('"','').lower().split(",")
  L = list(map(word_value,words))
  fp.close()
  return sum(list(l in twords for l in L))

print(p42())
