#Problem 10: Write a function unique to find all the unique elements of a list.
def unique(x):
	t=[]
	f=0
	for i in x:
		if f==0:
			t.append(i)
			f=1
		elif i not in t:
			t.append(i)
	print t
		
unique([1, 2, 1, 3, 2, 5])
