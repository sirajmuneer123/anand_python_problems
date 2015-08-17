'''
Problem 7: Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are replaced by a hyphen, typically used to create blog post URL from post title. It should also make sure there are no more than one hyphen in any place and there are no hyphens at the biginning and end of the slug.
'''
import string
def make_slug(str1):
	new_string=''
	flag=0
	for i in str1:
		if i in string.ascii_letters:
			new_string=new_string+i
			flag=1
		elif i in string.punctuation+' ' and flag==1:
			 new_string=new_string+'-'
			 flag=0
 	length=len(new_string)
	if new_string[length-1] in string.punctuation:
		new_string=new_string.strip(new_string[length-1])
	print new_string
make_slug("---- i n dexht m>l------->")
