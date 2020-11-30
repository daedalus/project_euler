def p4():
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]
    tmp=0
    for i in range(1,999):
        for j in range(1,999):
            tmp1 = i*j
            if is_palindrome(tmp1):
                if tmp1 > tmp:
                    tmp = tmp1
    return tmp

print(p4())
