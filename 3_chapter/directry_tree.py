'''
Problem 4: Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.
'''
import os
def tree(dirname,indent=0):
    	for i in range(indent):
        	print "|--",
    	print os.path.basename(dirname)
    	if os.path.isdir(dirname):
        	for files in os.listdir(dirname):
			tree(os.path.join(dirname,files),indent+1)
tree(os.getcwd())
