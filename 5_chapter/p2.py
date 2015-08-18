'''
a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters
'''
def print_all(filenames):
	for f in filenames:
		for line in open(f):
			if len(line)>40:
				print line,
print_all(['text.txt','text1.txt'])
