import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

y = np.random.normal(0, 1, 10000).cumsum(axis=0)
x = np.arange(y.size)

fig, ax = plt.subplots()
line, = ax.plot([], [], '.')
ax.margins(0.05)

def init():
    line.set_data(x[:2],y[:2])
    return line,

def animate(i):
    i = min(i, x.size)
    xdata = x[:i]
    ydata = y[:i]
    line.set_data(xdata, ydata)
    ax.relim()
    ax.autoscale()
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, interval=25)

plt.show()


