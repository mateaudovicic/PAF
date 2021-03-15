import matplotlib.pyplot as plot
import numpy as np
import math as m
from math import radians, cos, sin
from kinematika import jednoliko_gibanje, kosi_hitac

F = 60
m = 15
lista_v = []
lista_x = []
lista_a = []
lista_t = []
for t in np.arange(0.1, 10, 0.1):
    a = F / m
    v = a * t
    v = v + a * t
    x = v * t
    x = x + v * t
    a = v / t
    lista_a.append(a)
    lista_x.append(x)
    lista_v.append(v)
    lista_t.append(t)

jednoliko_gibanje(F, m, lista_a, lista_v, lista_x, lista_t)

v0 = 30
g = 9.81
alfa = radians(40)
t = np.arange(0, 10, 0.01)
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
    
kosi_hitac(v0, alfa, x1, y1, t_t, g)
