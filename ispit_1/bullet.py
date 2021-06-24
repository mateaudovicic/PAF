import math as m 
import numpy as np 
import matplotlib.pyplot as plt 


class Bullet:


    def init(self, h0, v0, dt = 0.01):
        self.h0 = h0
        self.y = h0
        self.v0 = v0 

        self.x = 0.
        self.vx = v0
        self.vy = 0.
        self.a = 0.
        self.t = 0.
        self.v = 0.
        self.dt = dt 

        self.__priv()

        self.x_x = []
        self.y_y = []
        self.t_t = []


    def __priv(self):
        print("Početna visina: {} m".format(self.h0))
        print("Početna brzina: {} m/s".format(self.v0))


    def reset(self):
        self.h0 = 0.
        self.y = 0.
        self.v0 = 0.
        self.x = 0.
        self.vx = 0.
        self.vy = 0.
        self.a = 0.
        self.t = 0.
        self.v = 0.
        self.dt = 0. 
        self.x_x.clear()
        self.y_y.clear()
        self.t_t.clear()


    def change_height(self, dh):
        self.y += dh
        print("Nova visina: {} m".format(self.y))


    def change_speed(self, dv):
        self.v0 += dv 
        print("Nova brzina: {} m/s".format(self.v0))


    def __move(self):
        self.x += self.v0 * self.dt 
        self.vy -= 9.81 * self.dt
        self.y += self.vy * self.dt 
        self.t += self.dt
        self.x_x.append(self.x)
        self.y_y.append(self.y)
        self.t_t.append(self.t)


    def plot_trajectory(self):
        while True:
            self.__move()
            if self.y <= 0:
                break
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        fig.suptitle('x-y, x-t, y-t (redom)')
        ax1.plot(self.x_x, self.y_y)
        ax2.plot(self.t_t, self.x_x)
        ax3.plot(self.t_t, self.y_y)
        plt.show()
        

    def velocity_to_hit_target(self, l, h, ri, rf, dt):
        self.x = 0.
        self.l = l
        self.h = h
        self.ri = ri
        self.rf = rf
        self.r = abs(self.rf + self.ri)
        self.dt = dt

        for self.v0 in range(1, 600):
            self.x = 0.
            self.y = self.h0
            self.vx = self.v0
            self.vy = 0.
            while self.y <= 0:
                self.__move()
                d =  m.sqrt((self.l - self.x)**2 + (self.r - self.y)**2)
                if d <= self.r:
                    break

        print("Potrebna početna brzina za pogoditi metu iznosi {} m/s.".format(self.v0))
    

    def air_resistance(self, l, h, ri, rf, dt, mass, k):
        self.l = l
        self.h = h
        self.ri = ri
        self.rf = rf
        self.r = abs(self.rf + self.ri)
        self.dt = dt

        for self.v0 in range(1, 600):
            self.x = 0.
            self.y = self.h0
            self.vx = self.v0
            self.vy = 0.
            while self.y <= 0:
                self.a = (9.81 + (k * self.v0) / mass)
                self.vx = self.v0 
                self.x += self.vx * self.dt 
                self.vy -= self.a * self.dt
                self.y += self.vy * self.dt  
                self.x_x.append(self.x)
                self.y_y.append(self.y)
                d =  m.sqrt((self.l - self.x)**2 + (self.r - self.y)**2)
                if d <= self.rf and d >= self.ri:
                    break

        print("Početna brzina s otporom zraka: {} m/s".format(self.v0))