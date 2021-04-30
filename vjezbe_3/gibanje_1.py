import particle_1 as prt
import math as m
import matplotlib.pyplot as plt
import domaci_rad_1 as do

p1 = prt.Particle(20, 30, 5, 5)
p1.printInfo()
rng = p1.range()

p2 = prt.Particle(15, 40, 3, 3)
p2.printInfo()
rng = p2.range()
print("Domet: {}".format(rng))
#p1.plot_trajectory()

# domaći rad 1

d1 = do.Particle(15, 40, 3, 3)
d1.range()
time = d1.total_time()
print("Ukupno vrijeme gibanja: {} s".format(time))
d1.reset()

"""d1 = do.Particle(20, 40, 10, 10)
speed = d1.max_speed()
print("Najveća brzina gibanja: {} m/s".format(speed))
d1.reset()

d1 = do.Particle(20, 40, 10, 10)
vel = d1.velocity_to_hit_target(45, 20, 20, 5)
print("Početna brzina potrebna za pogoditi metu: {} m/s".format((vel)))
d1.reset()

d1 = do.Particle(20, 40, 10, 10)
ang = d1.angle_to_hit_target(22, 20, 20, 5)
print("Kut otklona potreban za pogoditi metu: {} degrees".format(ang))
d1.reset()"""

"""d1 = do.Particle(20, 40, 10, 10)
d1.plot_trajectory2(30)
d1.reset()

d1 = do.Particle(20, 40, 10, 10)
d1.plot_trajectory3(30)
d1.reset()"""