import matplotlib.pyplot as plt
import numpy as np

print("Grafovi u prvih 10 sekundi jednolikog gibanja u jednoj dimenziji.")

#while True:
    #F = float(input("Unesite iznos sile u N: "))
    #if F < 0:
        #print("Pogrešan unos.")
    #else:
        #break
#while True:
    #m = float(input("Unesite iznos mase u kg: "))
    #if m < 0:
        #print("Pogrešan unos.")
    #else:
        #break
F = 60
m = 15

# v-t graf

lista_v = []
for t in np.arange(0.1, 10, 0.1):
    a = F / m
    v = a * t
    lista_v.append(v)
plt.ylabel('v(m/s)')
plt.xlabel('t(s)')
plt.title("v-t graf")
t = np.arange(0.1, 10, 0.1)
plt.plot(t, lista_v)
plt.show()

# x-t graf

lista_x = []
for t in np.arange(0.1, 10, 0.1):
    v = a * t
    x = v * t
    lista_x.append(x)
plt.ylabel('x(m)')
plt.xlabel('t(s)')
plt.title("x-t graf")
t = np.arange(0.1, 10, 0.1)
plt.plot(t, lista_x)
plt.show()

# a-t graf

lista_a = []
for t in np.arange(0.1, 10, 0.1):
    v = a * t
    a = v / t
    lista_a.append(a)
plt.ylabel('a(m/s^2)')
plt.xlabel('t(s)')
plt.title("a-t graf")
t = np.arange(0.1, 10, 0.1)
plt.plot(t, lista_a)
plt.show()

# subplot

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('v-t, x-t, a-t (redom)')
ax1.plot(t, lista_v)
ax2.plot(t, lista_x)
ax3.plot(t, lista_a)
plt.show()
