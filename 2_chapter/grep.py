#Problem 20: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
import sys
def grep(filename):
	for line in open(filename,'r+').readlines():
		if sys.argv[2] in line:
			print line,
grep(sys.argv[1])
