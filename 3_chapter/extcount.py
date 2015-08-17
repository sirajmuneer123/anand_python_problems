#Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.
import os
import sys
cwd=os.getcwd()
def count(cwd):
	list1=os.listdir(cwd)
	newlist=[]
	frequency ={}
	for i in list1:
		if os.path.isfile(i):
			newlist.append(i.split(".")[1])
	for j in newlist:
		frequency[j]=frequency.get(j,0)+1
	for key,value in frequency.items():
		print key ,value	

count(cwd)

		
