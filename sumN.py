def f(n):
	lst = []
	count = 0
	
	for i in range(0, n+1):
		count += i
		lst.append(count)

	return lst

	