'''
Problem 11: Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.
'''
import zipfile
import sys
z=zipfile.ZipFile(sys.argv[1],'w')
a=sys.argv[2:]
for i in a:
	z.write(i)
for i in z.namelist():
	print 
	print "file:",i 

