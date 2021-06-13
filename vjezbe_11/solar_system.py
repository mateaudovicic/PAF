import math as m 
import numpy as np 


class Solar_System:


    def init(self, m1, m2, r1, r2, v1, v2, dt = 60*6*24):
        self.m1 = m1
        self.m2 = m2
        self.r1 = r1 
        self.r2 = r2
        self.v1 = v1 
        self.v2 = v2
        self.a1 = 0.0
        self.a2 = 0.0
        self.dt = dt
        self.t = 0.0
        self.G = 6.67408 * (10**(-11))
        self.x_x1 = []
        self.y_y1 = []
        self.x_x2 = []
        self.y_y2 = []
        

    def reset(self):
        self.m1 = 0.0 
        self.m2 = 0.0
        self.r1 = 0.0
        self.r2 = 0.0
        self.v0 = 0.0 
        self.v1 = 0.0 
        self.v2 = 0.0
        self.a1 = 0.0
        self.a2 = 0.0
        self.dt = 0.0
        self.t = 0.0
        self.x_x1.clear()
        self.y_y1.clear()
        self.x_x2.clear()
        self.y_y2.clear()


    def __acceleration_1(self, r1, r2):
        d1 = m.sqrt((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2)
        return ((- self.G * self.m2) / (d1**3)) * np.subtract(r1,r2)


    def __acceleration_2(self, r1, r2):
        d2 = m.sqrt((r2[0] - r1[0])**2 + (r2[1] - r1[1])**2)
        return ((- self.G * self.m1) / (d2**3)) * np.subtract(r2,r1)

    
    def move(self, T):
        while self.t <= T:
            self.a1 = (self.__acceleration_1(self.r1, self.r2))
            self.v1 = np.add(self.v1, self.a1 * self.dt)
            self.r1 = np.add(self.r1, self.v1 * self.dt)
            self.a2 = (self.__acceleration_2(self.r1, self.r2))
            self.v2 = np.add(self.v2, self.a2 * self.dt) 
            self.r2 = np.add(self.r2, self.v2 * self.dt)
            self.x_x1.append(self.r1[0])
            self.y_y1.append(self.r1[1])
            self.x_x2 .append(self.r2[0])
            self.y_y2.append(self.r2[1])
            self.t += self.dt