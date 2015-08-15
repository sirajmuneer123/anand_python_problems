#Problem 27: Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.
def triplets(n):
	return [(i,j,k) for i in range(1,n) for j in range(i,n) for k in range(j,n) if i+j==k]
print triplets(5)
