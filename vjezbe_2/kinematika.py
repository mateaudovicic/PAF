import matplotlib.pyplot as plot
import numpy as np
import math

def jednoliko_gibanje(F, m, lista_a, lista_v, lista_x, lista_t):
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

def kosi_hitac(v0, alfa, x1, y1, t_t, g):
    
    plot.ylabel('y(m)')
    plot.xlabel('x(m)')
    plot.title("x-y graf")
    plot.ylim(0, 40)
    plot.xlim(0, 100)
    plot.plot(x1, y1)
    plot.show()

    
    plot.ylabel('x(m)')
    plot.xlabel('t(s)')
    plot.title("x-t graf")
    plot.ylim(0, 50)
    plot.xlim(0, 5)
    plot.plot(t_t, x1)
    plot.show()

    
    plot.ylabel('y(m)')
    plot.xlabel('t(s)')
    plot.title("y-t graf")
    plot.ylim(0, 25)
    plot.xlim(0, 2)
    plot.plot(t_t, y1)
    plot.show()

    fig, (ax1, ax2, ax3) = plot.subplots(3)
    fig.suptitle('x-y, x-t, y-t (redom)')
    ax1.plot(x1, y1)
    ax2.plot(t_t, x1)
    ax3.plot(t_t, y1)
    plot.show()
