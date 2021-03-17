import matplotlib.pyplot as plt
import numpy as np
import math as m
from zdk_4b import graf, h_max, domet, v_max, meta_putanja, udaljenost

v0 = 30
g = 9.81
alfa = (np.pi/4)
t = np.arange(0, 10, 0.1)
vx = v0 * m.cos(alfa)
vy = v0 * m.sin(alfa)
x = 0
y = 0

p = 20
q = 20
r = 5

t_t = []
x1 = []
y1 = []
d_d = []
#for t in range(0, 10):
for t in np.arange(0, 10, 0.01):
    x = x + vx * t 
    vy = vy - g * t
    y = y + vy * t
    x1.append(x)
    y1.append(y)
    t_t.append(t)
    #for i in range (t):
        #d = ((x1[i] - p)**2 + (y1[i] - q)**2) - r**2
        #d_d.append(d)

for t in np.arange(0, 10, 0.01):
#for t in np.arange(0, 10, 0.01):
    #print("t: {}".format(t))
    x = x + vx * t 
    vy = vy - g * t
    y = y + vy * t
    x1.append(x)
    y1.append(y)
    t_t.append(t)
    #for i in np.arange(0, t, 0.01):
    for i in range(len(x1)):
        d = m.sqrt((x1[i] - p)**2 + (y1[i] - q)**2)
        """print("m")
        print(x1[i])
        print(y1[i])
        print(d)"""
        d_d.append(d)
        

graf(v0, alfa, x1, y1, t, g)
h_max(v0, g, alfa)
domet(v0, g, alfa)
v_max(v0)
udaljenost(d_d, r)
meta_putanja(p, q, r, v0, alfa, x1, y1, t_t, g)