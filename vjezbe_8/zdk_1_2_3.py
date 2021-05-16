import Projectile as pro
import matplotlib.pyplot as plt
import numpy as np

p1 = pro.Projectile()


# 1. i 2. zadatak (Euler i Runge-Kutta s otporom zraka)


p1.init(60, 10, 0.5, 10, 0, 0, 0)
x1, y1, nn = p1.with_air_resistance_eu()
plt.plot(x1, y1, label = "Euler's method")
p1.reset()

p1.init(60, 10, 0.5, 10, 0, 0, 0)
x2, y2 = p1.with_air_resistance_rk()
plt.plot(x2, y2, label = "Ruge-Kutta method")
plt.legend()
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("x-y graph")
plt.show()
p1.reset()


# 3. zadatak (ovisnost dometa o Cx i masi)


def Cx_range():
        eul_eul = []
        rkt_rkt = []
        cx_cx = []
        for i in np.arange(0.0, 5.0, 0.1):
            cx_cx.append(i)
            p1.init(60, 10, 0.5, 10, 0, 0, 0, 0.01, i, 1.28)
            e, n, nn = p1.with_air_resistance_eu()
            eul_eul.append(max(e))
            p1.reset

            p1.init(60, 10, 0.5, 10, 0, 0, 0, 0.01, i, 1.28)
            r, m = p1.with_air_resistance_rk()
            rkt_rkt.append(max(r))
            p1.reset()
                        
        plt.plot(cx_cx, eul_eul, label = "Euler's method")
        plt.plot(cx_cx, rkt_rkt, label = "Runge-Kutta method")
        plt.legend()
        plt.title("Influence of Cx on range of projectile")
        plt.show()

Cx_range()


def mass_range():
        eul_eul = []
        rkt_rkt = []
        mass_mass = []
        for i in np.arange(0.1, 5.0, 0.1):
            mass_mass.append(i)
            p1.init(60, 10, 0.5, i, 0, 0, 0)
            e, n, nn = p1.with_air_resistance_eu()
            eul_eul.append(max(e))
            p1.reset

            p1.init(60, 10, 0.5, i, 0, 0, 0)
            r, m = p1.with_air_resistance_rk()
            rkt_rkt.append(max(r))
            p1.reset()

        plt.plot(mass_mass, eul_eul, label = "Euler's method")
        plt.plot(mass_mass, rkt_rkt, label = "Runge-Kutta method")
        plt.legend()
        plt.title("Influence of mass on range of projectile")
        plt.show()

mass_range()