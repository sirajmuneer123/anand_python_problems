'''
Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only.
'''
def mul(x,y):
	if y==0:
		return 0
	else:
		return x+mul(x,y-1)
print mul(0,4)
