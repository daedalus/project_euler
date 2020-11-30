def p2():
	l= 4*(10**6)
	# print(l)
	tmp = 0
	tmp2 = 2
	a = 1
	b = 2
	while (tmp <= l):
		tmp = a + b
		print(a,b,tmp)
		a = b
		b = tmp
		if tmp % 2 == 0:
			tmp2 += tmp
	return tmp2

print(p2())
