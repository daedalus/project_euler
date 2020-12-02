def T(n):
  return (n*(n+1))//2 # https://en.wikipedia.org/wiki/Triangular_number

def cfac(num):
  i = 2
  k = 2
  while i <= num//i:
     if num % i == 0:
       k += 2
     i += 1
  return k

def p12(l):
  n=1
  while True:
    num = T(n)
    dc = cfac(num)
    print(n,num,dc)
    n+=1
    if dc >= l:
      break
  return num

if __name__ == "__main__":
  print(p12(500))

