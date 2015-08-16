'''
Problem 30: Write a python function parse_csv to parse csv (comma separated values) files.
'''
import re
new=[]
def parse_csv(file):
  f=open(file,'r')
  txt=f.readlines()
  for l in txt:
    s=re.findall('\w+',l)
    new.append(s)
  print new
parse_csv('array.py')
