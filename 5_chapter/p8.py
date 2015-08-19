'''
 function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.
'''
def peep(it):
	list1=[]
	for i in it:
		list1.append(i)
	return list1[0],list1
it=iter(range(5))
x,it1=peep(it)	
print x,list(it1)
