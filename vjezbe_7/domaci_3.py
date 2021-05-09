import matplotlib.pyplot as plt
import ast

with open('vectors.txt', 'r') as file:
    content = file.readlines()
    #content = file.read().splitlines()

    x0_ = (content[0].split(" "))
    v0_ = (content[1].split(" "))
    a_ = (content[2].split(" "))
    t_ = (content[3].split(" "))

    x_x = []
    v_v = []
    a_a = []
    t_t = []
#.astype(float)
    for item in x0_:
        x_x.append(float(item))
    for item in v0_:
        v_v.append(float(item))
    for item in a_:
        a_a.append(float(item))
    for item in t_:
        t_t.append(float(item))

    """x_x = [float(idx) for idx in x0_.split(', ')]
    v_v = [float(idx) for idx in v0_.split(', ')]
    a_a = [float(idx) for idx in a_.split(', ')]
    t_t = [float(idx) for idx in t_.split(', ')]"""


    """x_x = map(float, x0_)
    v_v = map(float, v0_)
    a_a = map(float, a_)
    t_t = map(float, t_)"""

    """x_x = [float(x) for x in x0_]
    v_v = [float(x) for x in v0_]
    a_a = [float(x) for x in a_]
    t_t = [float(x) for x in t_]"""

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.suptitle("Harmonic oscillator in c++")

ax1.plot(t_t, x_x)
ax1.set_title("x-t graph")
ax1.set_xlabel("t [s]")
ax1.set_ylabel("x [m]")

ax2.plot(t_t, v_v)
ax2.set_title("v-t graph")
ax2.set_xlabel("t [s]")
ax2.set_ylabel("v [m/s]")

ax3.plot(t_t, a_a)
ax3.set_title("a-t graph")
ax3.set_xlabel("t [s]")
ax3.set_ylabel("a [m/$s^2$]")
plt.show()