""" 
	Write a function to compute the factorial
	of an integer.
	One iteratively and the other recursively.
"""


def factorial(x):
	ans = 1
	if x == 0 or x == 1:
		return ans
	elif x > 1:
		while x > 0:
			ans = x*ans
			x -= 1
		return ans
	
def factorial(x):
	if x == 0 or x == 1:
		return 1
	else:
		return x * factorial(x-1)

