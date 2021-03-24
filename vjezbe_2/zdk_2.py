import numpy as np
import matplotlib.pylab as plot
import math as m

v0 = 30
g = 9.81
alfa = (45/180) * m.pi
vx = v0 * m.cos(alfa)
vy = v0 * m.sin(alfa)
x = 0
y = 0
t_t = []
x1 = []
y1 = []

#for t in np.arange(0, 10, 0.01):

N = 100
dt = 0.1
t = 0
for i in range(N):
    t = t + dt
    x = x + vx * dt 
    vy = vy - g * dt
    y = y + vy * dt
    x1.append(x)
    y1.append(y)
    t_t.append(t)
plot.plot(x1, y1)
plot.ylabel('y(m)')
plot.xlabel('x(m)')
plot.title("x-y graf")
plot.show()

# x-t graf

plot.plot(t_t, x1)
plot.ylabel('x(m)')
plot.xlabel('t(s)')
plot.title("x-t graf")
plot.show()

# y-t graf

plot.plot(t_t, y1)
plot.ylabel('y(m)')
plot.xlabel('t(s)')
plot.title("y-t graf")
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
