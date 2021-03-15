import matplotlib.pyplot as plt
import numpy as np
import math as m

def graf(v0, alfa, x1, y1, t, g):
    #plt.ylim(0, 2000)
    #plt.xlim(0, 2000)
    plt.ylabel('y(m)')
    plt.xlabel('x(m)')
    plt.title("x-y graf")
    plt.ylim(0, 40)
    plt.xlim(0, 100)
    plt.plot(x1, y1)
    plt.show()

def h_max(v0, g, alfa):
    h = (v0 ** 2 / 2*g) * (np.sin(alfa))**2
    print("Maksimalna visina: {}".format(h))

def domet(v0, g, alfa):
    D = (v0 ** 2 / g) * np.sin(2*alfa)
    print("Domet: {}".format(D))
    
def v_max(v0):
    print("Maksimalna brzina: {}".format(v0))

def meta_putanja(p, q, r, v0, alfa, x1, y1, t, g):
    circle1 = plt.Circle((p, q), r, color='r')
    plt.gca().add_patch(circle1)
    plt.ylabel('y(m)')
    plt.xlabel('x(m)')
    plt.title("meta")
    plt.ylim(0, 40)
    plt.xlim(0, 100)
    plt.plot(x1, y1)
    plt.show()

def udaljenost():
    ...
    #print("Udaljenost od mete: {}".format())
    