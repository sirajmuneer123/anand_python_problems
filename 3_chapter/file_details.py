#Problem 3: Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.

#Hint: see help for os.stat.
import os
import time
cwd=os.getcwd()
list=os.listdir(cwd)
print "                                      "
print "FILE_NAME\t\tLENGTH\tMODIFICATION_DATE"
print "-------------------------------------------------------------------"
for i in list:
	if os.path.isfile(i):
		print i,"\t\t",len(i),"\t",time.ctime(os.stat(i).st_mtime)
