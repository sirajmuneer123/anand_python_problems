'''
Implement a function izip that works like itertools.izip
'''
def izip(x,y):
	length=len(x)
	for i in range(length):
		print x[i],y[i]
	
	
izip(['a','b','c'],[1,2,3])
