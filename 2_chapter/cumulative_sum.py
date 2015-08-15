#Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?
def cumulative_sum(num):
	sum=[]
	temp=0
	i=0
	while i!=len(num):
		temp=temp+num[i]
		sum.append(temp)
		i=i+1
	
	print "cumulative sum is=%s" %sum
cumulative_sum([1,2,3])
