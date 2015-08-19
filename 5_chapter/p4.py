'''
Write a function to compute the number of python files (.py extension) in a specified directory recursively.
'''
import os
def pfile(dir_name):
	count=0
	print dir_name
	for dirs,root,files in os.walk(dir_name):
		for f in files:
			if '.py' in f:
				count +=1
				print f
	print 'Number of .py files = ',
	print count
pfile(os.getcwd())
