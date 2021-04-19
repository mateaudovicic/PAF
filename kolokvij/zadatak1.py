import math as m
import matplotlib.pyplot as plt
import numpy as np

class VertikalniHitac:
    def __init__(self, v0, h0, dt = 0.01):
        self.v0 = v0
        self.dt = dt
        self.h0 = h0
        self.x0 = 0
        self.k = 5
        self.m = 10
        self.Fot = 0
        self.x_x = []
        self.h_h = []
        self.v_v = []
        self.t_t = []
        self.v_v.append(self.v0)
        self.h_h.append(self.h0)
        t = 0
        self.t_t.append(t)


    def reset(self):
        self.v0 = 0
        self.h0 = 0
        self.x0 = 0
        self.dt = 0
        self.v = 0
        self.s = 0
        self.x_x = []
        self.h_h = []
        self.v_v = []
        self.s_s = []
        self.t_t = []
    

    def printInfo(self):
        print("Uspješno stvoren objekt, njegova početna visina i brzina: {} m/s, {} m".format(self.v0, self.h0))


    def change_v0(self, new_v0):
        self.v0 = new_v0
        print("Nova početna brzina: {} m/s".format(self.v0))


    def change_h0(self, new_h0):
        self.h0 = new_h0
        print("Nova početna visina: {} m".format(self.h0))


    def move(self, t):
        self.a = -(self.k/ self.m) * self.h0
        self.v0 = self.v0 + self.a * t
        self.h0 = self.h0 + (self.v0 * t)
        self.v_v.append(self.v0)
        self.h_h.append(self.h0)

    
    def numeric(self):
        t = 0.0
        while self.h0 >= 0:
            self.move(self.dt)
            t += self.dt
            self.t_t.append(t)


    def plot_trajectory(self):
        plt.plot(self.t_t, self.h_h)
        plt.title("h-t graph")
        plt.xlabel("t [s]")
        plt.ylabel("h [m]")
        plt.show() 

        plt.plot(self.t_t, self.v_v)
        plt.title("v-t graph")
        plt.xlabel("t [s]")
        plt.ylabel("v [m/s]") 
        plt.show()


    def max_h(self):
        while True:
            self.move(self.dt)
            if self.h0 < 0:
                break
        return max(self.h_h)


    def max_v(self):
        while True:
            self.move(self.dt)
            if self.h0 < 0:
                break
        return max(self.v_v)


    def total_time(self):
        self.dt = 0.05
        self.numeric()
        return max(self.t_t)

    
    def air_resistance(self, k_ot):
        self.a = 0
        self.k_ot = k_ot
        self.Fot = self.Fot + (- self.k_ot * self.v0)
        self.a = self.a + (self.Fot / self.m)
        self.v0 = self.v0 + self.a * self.dt
        self.h0 = self.h0 + (self.v0 * self.dt)
        if self.h0 < 0:
            self.v_v.append(self.v0)
            self.h_h.append(self.h0)
        

    def numeric2(self):
        self.dt = 0.01
        t = 0.0
        self.air_resistance(0.5)
        for i in range(len(self.h_h)):
            t += self.dt
            self.t_t.append(t)
        return max(self.v_v), max(self.h_h), max(self.t_t)