'''
Problem 1: Write a program to list all files in the given directory.
'''
import os
cwd=os.getcwd()
list=os.listdir(cwd)
for i in list:
	if os.path.isfile(i):
		print i

