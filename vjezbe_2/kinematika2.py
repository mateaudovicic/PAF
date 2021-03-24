from math import radians
from kinematika import jednoliko_gibanje, kosi_hitac

F = 60
m = 15
jednoliko_gibanje(F, m)

v0 = 30
g = 9.81
alfa = radians(40)
kosi_hitac(v0, alfa, g)
