'''
Problem 5: Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.

'''
import urllib
import os
import sys
url = sys.argv[1]
response = urllib.urlopen(url)
base=os.path.basename(url)
if url[-1]=='/':
	print "saving %s as index.html"%url
else:
	print "saving %s as interpreter.html"%url
