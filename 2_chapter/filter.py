#Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.
def filter(f,a):
	return [i for i in a if f(i)==True]
def even(x):
	return x%2==0
print filter(even,range(15))
