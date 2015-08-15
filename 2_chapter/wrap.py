#Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
import sys
def wrap(filename,width):
	index=1
	width=int(width)
	for line in open(filename,'r+').readlines():
		for char in line:
			s=index % width
			if s==0:
				print "\n"
			else:
				print char,
				index=index+1
wrap(sys.argv[1],sys.argv[2])
