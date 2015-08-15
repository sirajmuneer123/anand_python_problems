#Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.
def cumulative_product(num):
	sum=[]
	temp=1
	i=0
	while i!=len(num):
		temp=temp*num[i]
		sum.append(temp)
		i=i+1
	
	print "cumulative product is=%s" %sum
cumulative_product([1,2,3,4,5])
