import subprocess
import re

def ebtables():
	string = subprocess.check_output(['sudo', 'ebtables', '-L', '--Lc'])

	count = 0
	for row in string:
		count += 1

	print count 

ebtables()