import sys
import subprocess
import os
from lib import settings
from config_tracker import get_problem

BASE_DIR = settings.PARENT_DIR # keeping learnpython as basedir in this file

def readsolnfile(dirname):
	with open(os.path.join(BASE_DIR,'problems',dirname,'solution.md'), 'r') as fin:
		print fin.read()


def readhintfile(dirname):
	with open(os.path.join(BASE_DIR,'problems',dirname,'solution.md'),'r') as fin:
		print fin.read()


def readprobfile(dirname):
	with open(os.path.join(BASE_DIR,'problems',dirname,'solution.md'),'r') as fin:
		print fin.read()


def checker():
	problem = get_problem()
	ans_file = sys.argv[2]
	orig_ans = subprocess.check_output(["python",BASE_DIR+'/'+problem+ "/solution.py"])
	givn_ans = subprocess.check_output(["python",ans_file])
	if orig_ans == givn_ans: 
		readsolnfile(problem) # change this with a display method comparison
	else:
		readhintfile(problem) # change this with a display method comparison showing the faults
	sys.exit()


def main():
	problem = get_problem()
	if len(sys.argv) == 1:
		os.system('python menu.py')
		os.exit()
	if len(sys.argv) > 3:
		print "Usage: learnpython verify program.py"
		sys.exit()
	if sys.argv[1] == "verify":
		try:
			checker()
		except:
			print "Usage: learnpython verify program.py"
	elif sys.argv[1] == "print":
		readprobfile(problem)
	else:
		problem = sys.argv[1]
		if problem in os.listdir(os.path.join(BASE_DIR,problems)):
			readprobfile(problem)
			sys.exit(1)
		else:
			os.system('python menu.py')


if __name__ == "__main__":
	main()