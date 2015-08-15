#Problem 3: What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.
def sum(x):
	s=''
	for i in x:
		s=s+i
	return s
print sum(['siraj','muneer','kk'])
		
		
