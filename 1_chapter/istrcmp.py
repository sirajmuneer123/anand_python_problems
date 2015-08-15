#Problem 13: Write a function istrcmp to compare two strings, ignoring the case.
def istrcmp(x,y):
	x=x.upper()
	y=y.upper()
	if x in y:
		return True
	else:
		return False
print istrcmp('skIraj','siraj')
