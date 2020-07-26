import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.dates as mdates
import datetime
import numpy as np
import time

def update_graph(id):
	Datum = [ line.strip('\n').split(",") for line in open('results.txt')][1:]
	Time = [ datetime.datetime.strptime(line[0],"%H:%M:%S") for line in Datum ]
	Time1 = [ mdates.date2num(line) for line in Time ]
	Byte = [ float(line[1]) for line in Datum ]

	order = np.argsort(Time1)
	xs = np.array(Time1)
	ys = np.array(Byte)

	fig, ax = plt.subplots(figsize=(10, 4))

	ax.set_title('data')
	ax.set_xlabel('Time')
	ax.set_ylabel('bytes')
	ax.plot_date(xs, ys, 'k-')
	plt.style.use('bmh')
	hfmt = mdates.DateFormatter('%H:%M:%S')
	ax.xaxis.set_major_formatter(hfmt)
	plt.gcf().autofmt_xdate()
        

	plt.savefig('static/bandwidth{}.png'.format(id))





    
    
