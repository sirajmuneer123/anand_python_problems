'''
Problem 8: Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.

'''
import urllib
import re
import sys
url=sys.argv[1]
#connect to a URL
website = urllib.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

for i in links:
	print i,"\n"

