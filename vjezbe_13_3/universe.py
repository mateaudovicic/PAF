import math 
import numpy as np 
import matplotlib.pyplot as plt 


class Planet:


    def __init__(self, name, color, mass, radius, r0, v0):
        self.name = name
        self.color = color
        self.mass = mass
        self.r0 = r0 
        self.v0 = v0
        self.radius = radius
        self.x_x = []
        self.y_y = []


class Universe:


    def __init__(self):
        self.dt = 0.0
        self.T = 0.0
        self.G = 6.67408 * (10**(-11))
        self.t = 0.0
        self.d = 0.0
        self.p_planets = []
        self.d_d = []


    def add_planet(self, planet):
        self.p_planets.append(planet)


    def __acceleration(self, m1, m2, r1, r2, rs1, rs2):
        self.d = math.sqrt((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2)
        self.d_d.append(self.d)
        if self.d <= (rs1 + rs2):   # ista stvar kao u liniji 57
            self.T = 0
        return ((- self.G * m2) / (self.d**3)) * np.subtract(r1, r2)


    def evolve(self, T, dt):
        self.T = T
        self.dt = dt
        while self.t <= self.T:
            for planet in self.p_planets:
                planet.a = np.array([0, 0])
                for p2 in self.p_planets:
                    if p2 == planet:
                        a = 0.0
                    else:
                        a = (self.__acceleration(planet.mass, p2.mass, planet.r0, p2.r0, planet.radius, p2.radius)) 
                        planet.a = np.add(planet.a, a)
                        if self.d <= (planet.radius + p2.radius):   # ista stvar kao u liniji 40 (samo što ne ulazi ni u jednu ni drugu petlju...)
                            break
                planet.v0 = np.add(planet.v0, planet.a * self.dt)
                planet.r0 = np.add(planet.r0, planet.v0 * self.dt)
                planet.x_x.append(planet.r0[0])
                planet.y_y.append(planet.r0[1])               
                    
            self.t += self.dt
        print("min(d_d): {}".format(min(self.d_d)))  # u self.d_d su udaljenosti za sve planete skupa