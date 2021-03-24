import matplotlib.pyplot as plt
import numpy as np
import math as m

def graf(v0, alfa, g, p, r, q):
    t_t = []
    x1 = []
    y1 = []
    d_d = []
    vx = v0 * m.cos(alfa)
    vy = v0 * m.sin(alfa)
    x = 0
    y = 0
    for t in np.arange(0, 10, 0.01):
        x = x + vx * t 
        vy = vy - g * t
        y = y + vy * t
        x1.append(x)
        y1.append(y)
        t_t.append(t)
    plt.ylabel('y(m)')
    plt.xlabel('x(m)')
    plt.title("x-y graf")
    plt.ylim(0, 40)
    plt.xlim(0, 100)
    plt.plot(x1, y1)
    plt.show()

def h_max(v0, g, alfa):
    y1 = []
    vy = v0 * m.sin(alfa)
    y = 0
    for t in np.arange(0, 10, 0.01): 
        vy = vy - g * t
        y = y + vy * t
        y1.append(y)
    print("Maksimalna visina: {} m".format(max(y1)))


def domet(v0, g, alfa):
    x1 = []
    vx = v0 * m.cos(alfa)
    x = 0
    while True:
        for t in np.arange(0, 10, 0.01):
            x = x + vx * t
            if x >= 0:
                x1.append(x)
            else:
                break
    print("Domet: {} m".format(max(x1)))
    
def v_max(v0, alfa, g):
    v = []
    vy = v0 * m.sin(alfa)
    for t in np.arange(0, 10, 0.01):
        vy = vy - g * t
        v.append(vy)
    print("Maksimalna brzina: {} m/s".format(max(v)))

def meta_putanja(p, q, r, v0, alfa, g):
    t_t = []
    x1 = []
    y1 = []
    d_d = []
    vx = v0 * m.cos(alfa)
    vy = v0 * m.sin(alfa)
    x = 0
    y = 0
    for t in np.arange(0, 10, 0.01):
        x = x + vx * t 
        vy = vy - g * t
        y = y + vy * t
        x1.append(x)
        y1.append(y)
        t_t.append(t)
    circle1 = plt.Circle((p, q), r, color='r')
    plt.gca().add_patch(circle1)
    plt.ylabel('y(m)')
    plt.xlabel('x(m)')
    plt.title("meta")
    plt.ylim(0, 40)
    plt.xlim(0, 100)
    plt.plot(x1, y1)
    plt.show()

def udaljenost(r, v0, alfa, p, q, g):
    t_t = []
    x1 = []
    y1 = []
    d_d = []
    vx = v0 * m.cos(alfa)
    vy = v0 * m.sin(alfa)
    x = 0
    y = 0
    for t in np.arange(0, 10, 0.01):
        x = x + vx * t 
        vy = vy - g * t
        y = y + vy * t
        x1.append(x)
        y1.append(y)
        t_t.append(t)
        for i in range(len(x1)):
            d = m.sqrt((x1[i] - p)**2 + (y1[i] - q)**2)
            d_d.append(d)
    print("Udaljenost od središta mete: {}".format(min(d_d)))
    if r < min(d_d):
        u = min(d_d) -r
        print("Meta nije pogođena. Udaljenost od mete: {} m".format(u))
    else:
        print("Meta je pogođena.")
