import matplotlib.pyplot as plot
import numpy as np
import math as m
from math import pi
from kinematika import jednoliko_gibanje, kosi_hitac

F = 60
m = 15
lista_v = []
for t in np.arange(0.1, 10, 0.1):
    a = F / m
    v = a * t
    lista_v.append(v)

lista_x = []
for t in np.arange(0.1, 10, 0.1):
    v = a * t
    x = v * t
    lista_x.append(x)

lista_a = []
for t in np.arange(0.1, 10, 0.1):
    v = a * t
    a = v / t
    lista_a.append(a)

jednoliko_gibanje(F, m, lista_a, lista_v, lista_x, t)



# kosi hitac

v0 = 30
g = 9.81
alfa = (np.pi/4)
t = np.arange(0, 10, 0.1)

# x-y graf

x1 = []
y1 = []
for el in t:
    x = ((v0*el)*np.cos(alfa)) 
    y = ((v0*el)*np.sin(alfa))-((0.5*g)*(el**2))
    x1.append(x)
    y1.append(y)

t = np.arange(0, 10, 0.1)
x2 = []
for el in t:
    x = ((v0*el)*np.cos(alfa)) 
    x2.append(x)

t = np.arange(0, 10, 0.1)
y2 = []
for el in t:
    y = ((v0*el)*np.sin(alfa))-((0.5*g)*(el**2)) 
    y2.append(y)

kosi_hitac(v0, alfa, x1, y1, x2, y2, t, g)
