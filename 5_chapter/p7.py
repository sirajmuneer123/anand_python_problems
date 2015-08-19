'''
Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.
'''
import sys 
def split(n,filename):
		i=0
		n=int(n)
		f=open(filename)
		lines=f.read().split('\n')
		for line in range(0,len(lines),n):
			new_line=lines[line:line+n]
			new_file_name='file'+str(i)+'.txt'
			new_file=open(new_file_name,'w+')
			new_file.write('\n'.join(new_line))
			new_file.close()
			i=i+1
							
split(sys.argv[1],sys.argv[2])
