import numpy as np
import math as m
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, alfa, x0, y0, dt = 0.01):
        self.v0 = v0
        self.dt = dt
        self.alfa = m.radians(alfa)
        self.x0 = x0
        self.y0 = y0
        self.x_x = []
        self.y_y = []
        self.vx = self.v0 * m.cos(self.alfa)
        self.vy = self.v0 * m.sin(self.alfa)
        self.x_x.append(self.x0)
        self.y_y.append(self.y0)
            
    def printInfo(self):
        print("v0 = {0:.2f}, alfa = {1:.2f}, x0 = {2:.2f}, y0 = {3:.2f}".format(self.v0, self.alfa, self.x0, self.y0))

    def reset(self):
        self.v0 = 0
        self.alfa = 0
        self.x0 = 0
        self.y0 = 0
        self.x_x = []
        self.y_y = []
        self.vx = 0
        self.vy = 0

    def __move(self, t):
        self.x0 = self.x0 + self.vx * t 
        self.vy = self.vy - 9.81 * t
        self.y0 = self.y0 + self.vy * t     
        self.x_x.append(self.x0)
        self.y_y.append(self.y0)

    def range(self):
        O = self.x0
        while True:
            self.__move(self.dt)
            if self.y0 <= 0:
                break
        m = self.x0 - O
        return m
            
    def plot_trajectory(self):
        plt.plot(self.x_x, self.y_y)
        plt.ylabel('y(m)')
        plt.xlabel('x(m)')
        plt.title("x-y graf")
        plt.show()

# 2. zdk (vježbe)
    def analitic(self):
        a = ((self.v0**2) * m.sin(2 * self.alfa)) / 9.81
        return a