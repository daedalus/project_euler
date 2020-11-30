def p6(n):
    i = [x for x in range(1,n+1)]
    j = list(map(lambda a:a*a,i))
    k = sum(i) ** 2 
    l = sum(j)
    print(i,j,k,l)
    return abs(k-l)

print(p6(10))
print(p6(100))

