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
    print("Maksimalna visina: {} m".format(h))

def domet(v0, g, alfa):
    D = (v0 ** 2 / g) * np.sin(2*alfa)
    print("Domet: {} m".format(D))
    
def v_max(v0):
    print("Maksimalna brzina: {} m/s".format(v0))

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

def udaljenost(d_d, r):
    print(min(d_d))
    if r < min(d_d):
        #print("Meta je pogođena.")
        u = min(d_d) -r
        print("Meta nije pogođena. Udaljenost od mete: {} m".format(u))
    else:
        #u = min(d_d) -r 
        #print("Udaljenost od mete: {} m".format(min(d_d)))
        print("Meta je pogođena.")
    
    