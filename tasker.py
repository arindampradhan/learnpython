import sys

def readfile(fname):
	with open('./problems/'+fname+'problem.md', 'r') as fin:
    print fin.read()




if sys.argv == "hello-world":
	readfile('hello-world')



print "hello"
import os
print os.path.dirname(__file__)