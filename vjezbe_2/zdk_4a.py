import matplotlib.pyplot as plt
import numpy as np
import math
from math import sin, cos
from zdk_4b import graf, h_max, domet, v_max, meta_putanja, udaljenost

v0 = 30
g = 9.81
alfa = (np.pi/4)
t = np.arange(0, 10, 0.1)
vx = v0 * cos(alfa)
vy = v0 * sin(alfa)
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
        

graf(v0, alfa, x1, y1, t, g)
h_max(v0, g, alfa)
domet(v0, g, alfa)
v_max(v0)
udaljenost()

p = 20
q = 20
r = 5
meta_putanja(p, q, r, v0, alfa, x1, y1, t_t, g)