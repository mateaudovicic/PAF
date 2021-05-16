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


# 2. zadatak (kut otklona)  - znam da krivo radi...


def angle_to_hit_target(p, q, r, v0, S, mass):
    alpha = 0.0
    for i in range(90):
        p1.reset()
        alpha += 0.1
        p1.init(alpha, v0, S, mass, p, q, r)
        x, y, d = p1.with_air_resistance_eu()
        for i in range(len(d)):
            if i <= r:
                angle = m.degrees(alpha)
                break
    print("Angle to hit target: {}°".format(angle))
    plt.plot(x, y)
    circle = plt.Circle((p, q), r, color='r', fill = False)
    plt.gca().add_patch(circle)
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.title("x-y graph")
    plt.show()

angle_to_hit_target(1, 1, 5, 60, 0.5, 10)
angle_to_hit_target(2, 1, 7, 50, 0.7, 9)