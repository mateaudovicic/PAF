import particle_1 as prt
import math as m

p1 = prt.Particle(20, 40, 10, 10)
rng = p1.range()
print("Domet: {}".format(rng))
p1.plot_trajectory()

# 1. zdk (domaći 1)
time = p1.total_time()
print("Ukupno vrijeme gibanja: {} s".format(time))

speed = p1.max_speed()
print("Najveća brzina gibanja: {} m/s".format(speed))

vel = p1.velocity_to_hit_target(45, 20, 20, 5)
print("Početna brzina potrebna za pogoditi metu: {} m/s".format((vel)))

ang = p1.angle_to_hit_target(22, 20, 20, 5)
print("Kut otklona potreban za pogoditi metu: {} degrees".format(ang))

# 2. zdk (domaći 1)
p1.plot_trajectory2(30)