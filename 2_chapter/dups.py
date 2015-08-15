#Problem 11: Write a function dups to find all duplicates in the list
def dups(x):
	l=len(x)
	nlist=[]
	for i in range(l):
		for j in range(i+1,l,1):
			if x[i]==x[j]:
				if x[i] in nlist:
					break	
				else:
					nlist.append(x[i])
					break
	print nlist
				
dups([1, 2, 1, 3, 2,1,3,3,3,3,3,3,3, 5])
