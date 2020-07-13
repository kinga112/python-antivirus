from time import *
from datetime import *
import csv

filename = "blocklist.csv.xlsx"

with open(filename, 'r') as csvfile:
    #create csv reader
    csvreader = csv.reader(csvfile)
    #print total number of rows and blocked
    print("Total no. of domains blocked: %d"%(csvreader.line_num))
    
host_path = r"/etc/hosts"
redirect = "127.0.0.1"
websites = [filename]

while True:  
    if datetime(datetime.now().year,datetime.now().month,datetime.now().day,9)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,17):
        print("working hours")
        with open(host_path,"r+") as fileptr:
            content = fileptr.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    fileptr.write(redirect+" "+website+"\n")
    else:
        print("Fun hours")
    sleep(5)