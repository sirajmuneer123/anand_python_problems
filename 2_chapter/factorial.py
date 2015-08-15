#Problem 5: Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?
array=[]
def factorial(number):
	while number!=0:
		array.append(number)
		number=number-1
	return array

def product(num):
	mul=1
	a=len(num)
	while a!=0:	
		mul=mul*num[a-1]
		a=a-1
	return mul

s=product(factorial(4))
print "factorial is =%s" % s


