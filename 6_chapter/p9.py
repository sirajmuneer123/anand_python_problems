"""
Problem 9: Write a function permute to compute all possible permutations of elements of a given list.

"""
def permute(list1,index=0,result=None,tmp=[]):
	if result == None:
		result=[]
		result.append(list1[:])
	else:
		copy(result,tmp)
	if index == len(list1):
		return result
	tmp=[]
	for j in result:
		for i in range(index+1,len(list1)):
			tmp.append(swap(j,index,i))
	permute(list1,index+1,result,tmp)
	return result

def copy(d,s):
	for i in s:
		d.append(i)
def swap(name,index,i):
	a_list=list(name)
	a_list[index],a_list[i] = a_list[i],a_list[index]
	return a_list
print permute([1, 2, 3])
