'''
Write a function to compute the total number of lines of code in all python files in the specified directory recursively.
'''
import os
def line_of_code(dir_name):
	i=0
	for dirs,root,files in os.walk(dir_name):
		for f in files:
			if '.py' in f:
				i=i+len(open(f).readlines())
	print i
line_of_code(os.getcwd())
