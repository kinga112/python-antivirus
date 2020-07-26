import subprocess
import re

def ebtables():
	string = subprocess.check_output(['sudo', 'ebtables', '-L', '--Lc'])
	pcnt = re.findall(r' pcnt = (.*?)\ -- ', string)
	# bcnt = re.findall(r' bcnt = (.*?)\-p ', string)
	
	count = 0
	for num in pcnt:
		count += int(num)

	print count

ebtables()