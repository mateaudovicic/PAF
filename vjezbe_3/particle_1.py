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

    def __move(self, t, p, q, r):
        self.x0 = self.x0 + self.vx * t 
        self.vy = self.vy - 9.81 * t
        self.y0 = self.y0 + self.vy * t     
        self.x_x.append(self.x0)
        self.y_y.append(self.y0)

        # 1. zdk (domaći 1)
        self.p = p
        self.q = q
        self.r = r
        self.d = m.sqrt((self.x0 - self.p)**2 + (self.y0 - self.q)**2)

    def range(self):
        O = self.x0
        while True:
            self.__move(self.dt, 0, 0, 0)
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

# 1. zdk (domaći 1)
    def total_time(self):
        t = 0.0
        for i in range(len(self.y_y)): 
            if i >= 0:
                self.__move(self.dt, 0, 0, 0)
                t += self.dt
        return t

    def max_speed(self):
        list_v = []
        self.__move(self.dt, 0, 0, 0)
        self.v = m.sqrt(self.vx**2 + self.vy**2)
        list_v.append(self.v)
        return max(list_v)

    def velocity_to_hit_target(self, beta, p, q, r):
        self.beta = m.radians(beta)
        self.p = p
        self.q = q
        self.r = r
        self.x0 = 0.0
        self.y0 = 0.0
        self.x_x.append(self.x0)
        self.y_y.append(self.y0)
        for self.v0 in np.arange(0.1, 100, 0.1):       
            self.vx = self.v0 * m.cos(self.beta)
            self.vy = self.v0 * m.sin(self.beta)
            self.__move(self.dt, self.p, self.q, self.r)
            #for i in range(len(self.x_x)):
                #d = m.sqrt((self.x_x[i] - self.p)**2 + (self.y_y[i] - self.q)**2)
            if self.d <= self.r:
                break
        return self.v0
        
    def angle_to_hit_target(self, v, p, q, r):
        self.v = v
        self.p = p
        self.q = q
        self.r = r
        self.x0 = 0.0
        self.y0 = 0.0
        self.x_x.append(self.x0)
        self.y_y.append(self.y0)
        for i in range(900): 
            self.alfa += 0.1
            self.alfa = m.radians(self.alfa)   
            self.vx = self.v * m.cos(self.alfa)
            self.vy = self.v * m.sin(self.alfa)
            self.__move(self.dt, self.p, self.q, self.r)
            #for i in range(len(self.x_x)):
                #d = m.sqrt((self.x_x[i] - self.p)**2 + (self.y_y[i] - self.q)**2)
            if self.d <= self.r:
                self.alfa = m.degrees(self.alfa)
                break
        return self.alfa

    # 2. zdk (domaći 1)
    def plot_trajectory2(self, v0):
        list_alfa = []
        list_range = []
        #list_time = []
        self.v0 = v0
        self.x0 = 0
        self.y0 = 0
        for alfa in range(90):
            self.alfa = alfa           
            list_alfa.append(alfa)
            self.alfa = m.radians(alfa)
            self.vx = self.v0 * m.cos(self.alfa)
            self.vy = self.v0 * m.sin(self.alfa)
            self.__move(self.dt, 0, 0, 0)
            R = self.range()
            list_range.append(R)
            #T = self.total_time()
            #list_time.append()
        plt.plot(list_alfa, list_range)
        plt.show()
        #plt.plot(list_alfa, list_time)
        #plt.show()