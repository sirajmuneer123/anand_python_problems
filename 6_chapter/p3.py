"""
Problem 3: Write a function unflatten_dict to do reverse of flatten_dict.
"""
def unflatten_dict(d,result=None):
	if result == None:
		result={}
	for key in d:
		if '.' in key:
			string='result'
			for i in key.split('.'):
				eval(string).setdefault(i,{}) 
				string += '[' + "'" + i + "'" + ']'
			exec(string + ' = d[key]') 
		else:
			result[key] = d[key]
	return result
print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
