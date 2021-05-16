import math as m
import matplotlib.pyplot as plt
import numpy as np


class Projectile:


    def init(self, alpha, v0, S, mass, p, q, r, dt = 0.01, Cx = 0.47, rho_air = 1.28):
        self.x = 0.0
        self.y = 0.0
        self.mass = mass
        self.alpha = m.radians(alpha)
        self.v0 = v0
        self.dt = dt
        self.t = 0.0
        self.ax = 0.0
        self.ay = 0.0
        self.x_x1 = []
        self.y_y1 = []
        self.x_x2 = []
        self.y_y2 = []
        self.d_d = []
        self.vx = v0 * m.cos(self.alpha)
        self.vy = v0 * m.sin(self.alpha)        
        self.S = S
        self.Cx = Cx
        self.rho_air = rho_air
        self.g = 9.81 
        self.p = p 
        self.q = q
        self.r = r 
        self.d = 0.0      


    def reset(self):
        self.x = 0.0
        self.y = 0.0
        self.v0 = 0.0
        self.alpha = 0.0
        self.dt = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = 0.0
        self.p = 0.0 
        self.q = 0.0
        self.r = 0.0
        self.d = 0.0
        self.x_x1.clear()
        self.y_y1.clear()
        self.x_x2.clear()
        self.y_y2.clear()
        self.d_d.clear()


# 1. zadatak (Euler)


    def with_air_resistance_eu(self):
        while self.y >= 0:
            self.vx += self.ax * self.dt    
            self.x += self.vx * self.dt
            self.ax = - abs((self.vx**2) * self.rho_air * self.Cx * self.S) / (2*self.mass)
            self.x_x1.append(self.x)

            self.vy += self.ay * self.dt      
            self.y += self.vy * self.dt
            self.ay = - self.g - abs((self.vy**2) * self.rho_air * self.Cx * self.S) / (2*self.mass)
            self.y_y1.append(self.y)

            # (za domaci_rad_4)

            self.d = m.sqrt((self.x - self.p)**2 + (self.y - self.q)**2)
            self.d_d.append(self.d)

        return self.x_x1, self.y_y1, self.d_d


# 2. zadatak (Runge-Kutta)


    def __acceleration_x(self, vx): 
        return (- abs((self.vx**2) * self.rho_air * self.Cx * self.S) / (2*self.mass))


    def __acceleration_y(self, vy): 
        return (- self.g - abs((self.vy**2) * self.rho_air * self.Cx * self.S) / (2*self.mass))


    def __runge_kutta(self):    
        k_1vx = self.__acceleration_x(self.vx) * self.dt 
        k_1x = self.vx * self.dt
        k_2vx = self.__acceleration_x(self.vx + (k_1vx / 2)) * self.dt
        k_2x = (self.vx + k_1vx/2) * self.dt
        k_3vx = self.__acceleration_x(self.vx + (k_2vx / 2)) * self.dt
        k_3x = (self.vx + (k_2vx / 2)) * self.dt
        k_4vx = self.__acceleration_x(self.vx + k_3vx) * self.dt
        k_4x = (self.vx + k_3vx) * self.dt
        self.vx += (1/6) * (k_1vx + 2*k_2vx + 2*k_3vx + k_4vx)
        self.x += (1/6) * (k_1x + 2*k_2x + 2*k_3x + k_4x)
        self.x_x2.append(self.x)
        
        k_1vy = self.__acceleration_y(self.vy) * self.dt 
        k_1y = self.vy * self.dt
        k_2vy = self.__acceleration_y(self.vy + (k_1vy / 2)) * self.dt
        k_2y = (self.vy + (k_1vy / 2)) * self.dt
        k_3vy = self.__acceleration_y(self.vy + (k_2vy / 2)) * self.dt
        k_3y = (self.vy + (k_2vy / 2)) * self.dt
        k_4vy = self.__acceleration_y(self.vy + k_3vy) * self.dt
        k_4y = (self.vy + k_3vy) * self.dt
        self.vy += (1/6) * (k_1vy + 2*k_2vy + 2*k_3vy + k_4vy)
        self.y += (1/6) * (k_1y + 2*k_2y + 2*k_3y + k_4y)
        self.y_y2.append(self.y)


    def with_air_resistance_rk(self):   
        while self.y >= 0:
            self.__runge_kutta()
        return self.x_x2, self.y_y2


# domaci_rad_4


    def sphere_cube(self, choice, r, a):
        if choice == 0:
            self.S = m.pi * (r**2)
        else:
            self.S = a**2
        s1, s2, nn = self.with_air_resistance_eu()
        return s1, s2