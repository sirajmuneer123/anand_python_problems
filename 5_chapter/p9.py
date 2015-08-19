'''
The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.
'''
def enumerate(x):
	length=len(x)
	y=[]
	for i in range(0,length-1,1):
		y.append(i)	
	return zip(y,x)
for i , c in enumerate(["a","b","c"]):
	print i, c
