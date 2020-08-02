import subprocess
import re

def ebtables():
	string = subprocess.check_output(['sudo', 'ebtables', '-L', '--Lc'])
	entries = re.findall(r'D, entries: (.*?)\,', string)
	print entries[0]

ebtables()