import matplotlib.pyplot as plt
import numpy as np

F = 60
m = 15

lista_v = []
lista_x = []
lista_a = []
lista_t = []
for t in np.arange(0.1, 10, 0.1):
    a = F / m
    v = a * t
    v = v + a * t
    x = v * t
    x = x + v * t
    a = v / t
    lista_x.append(x)
    lista_v.append(v)
    lista_a.append(a)
    lista_t.append(t)

# v-t graf

plt.ylabel('v(m/s)')
plt.xlabel('t(s)')
plt.title("v-t graf")
t = np.arange(0.1, 10, 0.1)
plt.plot(lista_t, lista_v)
plt.show()

# x-t graf

plt.ylabel('x(m)')
plt.xlabel('t(s)')
plt.title("x-t graf")
t = np.arange(0.1, 10, 0.1)
plt.plot(lista_t, lista_x)
plt.show()

# a-t graf

plt.ylabel('a(m/s^2)')
plt.xlabel('t(s)')
plt.title("a-t graf")
t = np.arange(0.1, 10, 0.1)
plt.plot(lista_t, lista_a)
plt.show()

# subplot

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('v-t, x-t, a-t (redom)')
ax1.plot(lista_t, lista_v)
ax2.plot(lista_t, lista_x)
ax3.plot(lista_t, lista_a)
plt.show()
