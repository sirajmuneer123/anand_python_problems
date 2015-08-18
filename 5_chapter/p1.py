'''
Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::
'''

def reverse(num):
	length=len(num)
	i=0
	temp=[]
	while length!=0:
		temp.append(num[length-1])
		length=length-1
        return iter(temp)
	
it=reverse([1,2,3,4,5,6,7])
print it.next()
