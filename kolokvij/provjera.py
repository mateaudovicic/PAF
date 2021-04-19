import zadatak1 as zad1
import math as m
import matplotlib.pyplot as plt

z1 = zad1.VertikalniHitac(30, 30)
z1.printInfo()
z1.change_v0(15)
z1.change_h0(15)
print("\n")

z2 = zad1.VertikalniHitac(10, 10)
z2.printInfo()
z2.numeric()
z2.plot_trajectory()
maxh = z2.max_h()
print("Maksimalna visina: {} m".format(maxh))
maxv = z2.max_v()
print("Maksimalna brzina: {} m".format(maxv))
time = z2.total_time()
print("Ukupno vrijeme trajanja gibanja: {} s".format(time))
print("\n")

z3 = zad1.VertikalniHitac(10, 10)
x, y, z = z3.numeric2()
print("Maksimalna brzina s otporom zraka: {} m/s".format(x))
print("Maksimalna visina s otporom zraka: {} m".format(y))
print("Ukupno vrijeme trajanja gibanja s otporom zraka: {} s".format(z))
print("\n")
print("Maksimalna brzina bez otpora zraka: {} m/s".format(maxv))
print("Maksimalna visina bez otpora zraka: {} m".format(maxh))
print("Ukupno vrijeme trajanja gibanja bez otpora zraka: {} s".format(time))
print("\n")
a = maxv - x
b = maxh - y
c = time - z
print("Razlika u maksimalnoj brzini: {}".format(a))
print("Razlika u maksimalnoj visini: {}".format(b))
print("Razlika u vremenu trajanja: {}".format(c))