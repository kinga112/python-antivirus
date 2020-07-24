import time
import psutil
import datetime
import sys
from time import gmtime, strftime


def main():
    old_value = 0
    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        
        if old_value:
            stat = send_stat(new_value - old_value)
            print(stat)
        
        old_value = new_value
        
        time.sleep(1)
        
def convert_to_gbit(value): #returns MB
    return value/1024./1024.*8

def send_stat(value):
    for i in range(0,100):
        time.sleep(0)
    f = open('results.txt', 'w', 'a')
    print ((strftime("%H:%M:%S", gmtime())),"%0.3f" % convert_to_gbit(value), file=f, sep=',')


main()
