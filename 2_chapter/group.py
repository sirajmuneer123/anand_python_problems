#Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.
def group(list1,size):
	new_list=[]
	t_list=[]
	j=0
	for i in list1:
		if j<size:
			t_list.append(i)
			j=j+1
		else:
			new_list.append(t_list)
			t_list=[]
			t_list.append(i)
			j=1
	if t_list is not 0:
		new_list.append(t_list)
	return new_list
print group([1,2,3,4,5,6,7,8],4)	
		
	
