import numpy as np
import matplotlib.pylab as plot
import math as m

v0 = 30
g = 9.81
alfa = (m.pi/4)
t = np.arange(0, 10, 0.1)

# x-y graf

x1 = []
y1 = []
for el in t:
    x = ((v0*el)*m.cos(alfa)) 
    y = ((v0*el)*m.sin(alfa))-((0.5*g)*(el**2))
    x1.append(x)
    y1.append(y)
plot.plot(x1, y1)
plot.ylabel('y(m)')
plot.xlabel('x(m)')
plot.title("x-y graf")
plot.ylim(0, 40)
plot.xlim(0, 100)
plot.show()

# x-t graf

t = np.arange(0, 10, 0.1)
x2 = []
for el in t:
    x = ((v0*el)*m.cos(alfa)) 
    x2.append(x)
plot.plot(t, x2)
plot.ylabel('x(m)')
plot.xlabel('t(s)')
plot.title("x-t graf")
plot.ylim(0, 50)
plot.xlim(0, 5)
plot.show()

# y-t graf

t = np.arange(0, 10, 0.1)
y2 = []
for el in t:
    y = ((v0*el)*m.sin(alfa))-((0.5*g)*(el**2)) 
    y2.append(y)
plot.plot(t, y2)
plot.ylabel('y(m)')
plot.xlabel('t(s)')
plot.title("y-t graf")
plot.ylim(0, 25)
plot.xlim(0, 5)
plot.show()

# subplot

fig, (ax1, ax2, ax3) = plot.subplots(3)
fig.suptitle('x-y, x-t, y-t (redom)')
#for ax in fig.get_axes():
    #ax.label_outer()
ax1.plot(x1, y1)
ax2.plot(t, x2)
ax3.plot(t, y2)
plot.show()
