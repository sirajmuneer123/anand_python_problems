#Problem 2: Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum.
def sum(x):
	s=0
	for i in x:
		s=s+i
	return s
print sum([1,2,3,4,5])
		
