#Problem 29: Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:
def array(list_num,list_val):
	return [[None]*list_val for i in range(list_num)]
print array(2,3)
