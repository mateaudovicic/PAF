import Projectile as pro
import matplotlib.pyplot as plt
import math as m

p1 = pro.Projectile()


# 1. zadatak (putanje sfere i kocke)


p1.init(60, 10, 0.5, 10, 0, 0, 0)
s1, s2 = p1.sphere_cube(0, 3, 5.3)
plt.plot(s1, s2, label = "sphere")
p1.reset()

p1.init(60, 10, 0.5, 10, 0, 0, 0)
c1, c2 = p1.sphere_cube(1, 3, 5.3)
plt.plot(c1, c2, label = "cube")
plt.legend()
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("x-y graph")
plt.show()
p1.reset()


# 2. zadatak (kut otklona) 


def angle_to_hit_target(p, q, r, v0, S, mass):
    alpha = 0.0
    dd_d = []
    aa_a = []
    while alpha < 87.0:
        p1.reset()
        alpha += 0.1
        p1.init(alpha, v0, S, mass, p, q, r)
        x, y, d = p1.with_air_resistance_eu()
        dd_d.append(d)
        aa_a.append(alpha)
    for i in range (len(dd_d)):
        if dd_d[i] <= r:
            p1.reset()
            p1.init(aa_a[i], v0, S, mass, p, q, r)
            x, y, d = p1.with_air_resistance_eu()
            break
    print("Angle to hit target: {}°".format(aa_a[i]))
    plt.plot(x, y)
    circle = plt.Circle((p, q), r, color='r', fill = False)
    plt.gca().add_patch(circle)
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.title("x-y graph")
    plt.show()

angle_to_hit_target(10, 10, 5, 30, 0.5, 10)
angle_to_hit_target(15, 15, 5, 40, 0.7, 9)
angle_to_hit_target(12, 10, 5, 35, 0.7, 9)