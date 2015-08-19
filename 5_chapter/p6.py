'''
Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively
'''
import os
import string
def ignore(dir_name):
        for dirs,root,files in os.walk(dir_name):
                for f in files:
                        for line in open(f).readlines():
				for i in line:
					if i in string.ascii_letters:
						print line,
						break
					elif i=='#' or i=='\n':
						break
					else:					
						print line,
						break
ignore(os.getcwd())

