import math 
import matplotlib.pyplot as plt
import particle_1 as p

list_dt = []
list_err = []
#p1 = p.Particle(10, 60, 0, 0, 0.0)
dt = 0.0
N = 100

for i in range(N):
    dt += 0.01
    list_dt.append(dt)
    p1 = p.Particle(10, 60 ,0, 0, dt)
    error = abs(p1.range() - p1.analitic()) / p1.analitic() *100
    list_err.append(error)

plt.plot(list_dt, list_err)
plt.ylabel("absolute relative error [%]")
plt.xlabel("dt [s]")
plt.title("Absolute relative error for range of projectile")
plt.show()