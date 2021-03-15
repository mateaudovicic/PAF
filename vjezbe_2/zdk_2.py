import numpy as np
import matplotlib.pylab as plot
import math as m

v0 = 30
g = 9.81
alfa = (np.pi/4)
t = np.arange(0, 10, 0.01)
vx = v0 * m.cos(alfa)
vy = v0 * m.sin(alfa)
x = 0
y = 0
t_t = []
x1 = []
y1 = []
for t in np.arange(0, 10, 0.01):
    x = x + vx * t 
    vy = vy - g * t
    y = y + vy * t
    x1.append(x)
    y1.append(y)
    t_t.append(t)
plot.plot(x1, y1)
plot.ylabel('y(m)')
plot.xlabel('x(m)')
plot.title("x-y graf")
plot.ylim(0, 40)
plot.xlim(0, 100)
plot.show()

# x-t graf

plot.plot(t_t, x1)
plot.ylabel('x(m)')
plot.xlabel('t(s)')
plot.title("x-t graf")
plot.ylim(0, 50)
plot.xlim(0, 5)
plot.show()

# y-t graf

plot.plot(t_t, y1)
plot.ylabel('y(m)')
plot.xlabel('t(s)')
plot.title("y-t graf")
plot.ylim(0, 25)
plot.xlim(0, 2)
plot.show()

# subplot

fig, (ax1, ax2, ax3) = plot.subplots(3)
fig.suptitle('x-y, x-t, y-t (redom)')
for ax in fig.get_axes():
    ax.label_outer()
ax1.plot(x1, y1)
ax2.plot(t_t, x1)
ax3.plot(t_t, y1)
plot.show()
