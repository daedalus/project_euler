def p7(n):
    tmp = [2]
    p=1
    while len(tmp) <= n-1:
        f = True
        p+=1
        for x in tmp:
            if p % x == 0:
                f = False
                break
        if f == True:
            tmp.append(p)
    return p
  
print(p7(10001))
