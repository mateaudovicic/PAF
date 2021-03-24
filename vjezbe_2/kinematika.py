import matplotlib.pyplot as plot
import numpy as np
import math as m

def jednoliko_gibanje(F, m):
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
    plot.ylabel('v(m/s)')
    plot.xlabel('t(s)')
    plot.title("v-t graf")
    plot.plot(lista_t, lista_v)
    plot.show()

    plot.ylabel('x(m)')
    plot.xlabel('t(s)')
    plot.title("x-t graf")
    plot.plot(lista_t, lista_x)
    plot.show()

    plot.ylabel('a(m/s^2)')
    plot.xlabel('t(s)')
    plot.title("a-t graf")
    plot.plot(lista_t, lista_a)
    plot.show()

    fig, (ax1, ax2, ax3) = plot.subplots(3)
    fig.suptitle('v-t, x-t, a-t (redom)')
    ax1.plot(lista_t, lista_v)
    ax2.plot(lista_t, lista_x)
    ax3.plot(lista_t, lista_a)
    plot.show()

def kosi_hitac(v0, alfa, g): 
    t_t = []
    x1 = []
    y1 = []  
    vx = v0 * m.cos(alfa)
    vy = v0 * m.sin(alfa)
    x = 0
    y = 0
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
    plot.ylabel('y(m)')
    plot.xlabel('x(m)')
    plot.title("x-y graf")
    plot.plot(x1, y1)
    plot.show()
 
    plot.ylabel('x(m)')
    plot.xlabel('t(s)')
    plot.title("x-t graf")
    plot.plot(t_t, x1)
    plot.show()

    plot.ylabel('y(m)')
    plot.xlabel('t(s)')
    plot.title("y-t graf")
    plot.plot(t_t, y1)
    plot.show()

    fig, (ax1, ax2, ax3) = plot.subplots(3)
    fig.suptitle('x-y, x-t, y-t (redom)')
    ax1.plot(x1, y1)
    ax2.plot(t_t, x1)
    ax3.plot(t_t, y1)
    plot.show()
