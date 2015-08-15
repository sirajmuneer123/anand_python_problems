#Problem 12: Write a function count_digits to find number of digits in the given number.
def count_digits(x):
	count=0
	while(x>0):
		count=count+1
		x=x/10
	return count
print count_digits(123456)
		
