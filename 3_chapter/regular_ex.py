'''
Problem 9: Write a regular expression to validate a phone number.
'''
import re
def reg_exp(str1):
	match=re.search(r'phone:\d\d\d\d\d\d\d|mobile:\d\d\d\d\d\d\d\d\d\d',str1)

	if match:
		print 'found'
		s= re.findall(r'phone:\d\d\d\d\d\d\d|mobile:\d\d\d\d\d\d\d\d\d\d',str1)
		for i in s:
			print i
	else:
		print 'not found'
reg_exp("mobile:3949499456 kjnbb nuphone:2 b[njk k[[nnkjuuphone:1234567")	


