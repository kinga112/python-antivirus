import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib import style
import itertools

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('results.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if line:
            pos = line.split(",")
            if len(pos) > 1:
                xs.append(pos[0])
                ys.append(pos[1])
    ax1.clear()
    ax1.plot(np.sort(xs), np.sort(ys))


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.ylim((0,10))
plt.show()