import numpy as np
import math as m
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, alfa, x0, y0):
        self.v0 = v0
        self.alfa = (alfa/180) * m.pi
        self.x0 = x0
        self.y0 = y0
        self.x_x = []
        self.y_y = []
        self.vx = v0 * m.cos(self.alfa)
        self.vy = v0 * m.sin(self.alfa)
        self.x_x.append(self.x0)
        self.y_y.append(self.y0)
        print(self.x_x)
        print(self.y_y)
            
    def printInfo(self):
        print("v0 = {0:.2f}, alfa = {1:.2f}, x0 = {2:.2f}, y0 = {3:.2f}".format(self.v0, self.alfa, self.x0, self.y0))

    def reset(self):
        self.v0 = 0
        self.alfa = 0
        self.x0 = 0
        self.y0 = 0

    def __move(self, t):
        #self.x_x = []
        #self.y_y = []
        #for t in np.arange(0, 10, 0.01):
        self.x0 = self.x0 + self.vx * t 
        self.vy = self.vy - 9.81 * t
        self.y0 = self.y0 + self.vy * t
            #self.x_x.append(self.x0)
            #self.y_y.append(self.y0)

    def range(self):
        ...

    def plot_trajectory(self):
        #self.x_x = []
        #self.y_y = []
        for t in np.arange(0, 10, 0.01):
            self.__move(t)
            self.x_x.append(self.x0)
            self.y_y.append(self.y0)
        self.res = self.x_x[::len(self.x_x)-1]  
        print(self.res)
        plt.ylabel('y(m)')
        plt.xlabel('x(m)')
        plt.title("x-y graf")
        plt.ylim(0, 20)
        plt.xlim(0, 50)
        plt.plot(self.x_x, self.y_y)
        plt.show()