def reverse(num):
	length=len(num)
	i=0
	temp=[]
	while length!=0:
		temp.append(num[length-1])
		length=length-1
        return temp
	
f=reverse([1,2,3,4,5,6,7])
print "revere is =%s" %f
