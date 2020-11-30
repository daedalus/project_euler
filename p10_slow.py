def sieve(n):
    tmp = [2]
    p=1
    while p <= n:
        f = True
        p+=1
        for x in tmp:
            if p % x == 0:
                f = False
                break
        if f == True:
            tmp.append(p)
    return tmp
  
def p10(n):
    return sum(sieve(n))

print(p10(2*(10**6)))
