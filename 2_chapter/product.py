#Problem 4: Implement a function product, to compute product of a list of numbers.
def product(num):
	mul=1
	a=len(num)
	while a!=0:	
		mul=mul*num[a-1]
		a=a-1
	return mul
s=product(w)
print "product =%s" % s

