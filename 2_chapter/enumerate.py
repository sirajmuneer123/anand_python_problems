#Problem 28: Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.
def enumerate(a_list):
	return [(i,a_list[j]) for i in range(len(a_list)) for j in range(len(a_list)) if i==j]
print enumerate(["a", "b", "c"])
