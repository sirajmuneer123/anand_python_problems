#Problem 25: Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.
def map(f,r):
	return [f(i) for i in r]
def squar(x):
	return x*x
print map(squar,range(5))

