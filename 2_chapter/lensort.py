#Problem 13: Write a function lensort to sort a list of strings based on length.
def lensort(a):
	a.sort(key=lambda x:len(x))
	return a
print lensort(['zz','zzz','z','python', 'perl', 'java', 'c', 'haskell', 'ruby'])
