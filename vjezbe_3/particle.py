import math as m
from math import fabs

class Particle:
    def __init__(self, mass, x_0):
        self.mass = mass
        self.x_0 = x_0

    def printInfo(self):
        print("Čestica ima masu {0:.2f} i u početnom trnutku nalazi se na polažaju x={1:.2f}".format(self.mass, self.x_0))

    def udaljenost(self):
        x = fabs(self.x_0)
        print("Udaljenost od ishodišta: {}".format(x))




