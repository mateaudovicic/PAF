import bungee as bng
import matplotlib.pyplot as plt

b0 = bng.BungeeJumping()
b0.init(70.0, 50.0, 200.0, 100.0, 0.0, 0.0, 0.001, 0.0, 0.0)
b0.move(50)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("Bungee Jumping")

ax1.plot(b0.t_t, b0.y_y)
ax1.set_title("y-t graph without air resistance")
ax1.set_xlabel("t $[s]$")
ax1.set_ylabel("y $[m]$")

ax2.plot(b0.t_t, b0.Ep_p, label = "Potential energy")
ax2.plot(b0.t_t, b0.Ek_k, label = "Kinetic energy")
ax2.plot(b0.t_t, b0.Eel_el, label = "Elastic energy")
ax2.plot(b0.t_t, b0.Etot_tot, label = "Total energy")
ax2.set_title("energy conservation")
ax2.set_xlabel("t $[s]$")
ax2.set_ylabel("E $[J]$")

b0.reset()

b1 = bng.BungeeJumping()
b1.init(70.0, 50.0, 200.0, 100.0, 0.0, 0.125)
b1.move(50)

ax3.plot(b1.t_t, b1.y_y)
ax3.set_title("y-t graph with air resistance")
ax3.set_xlabel("t $[s]$")
ax3.set_ylabel("y $[m]$")

ax4.plot(b1.t_t, b1.Ep_p, label = "Potential energy")
ax4.plot(b1.t_t, b1.Ek_k, label = "Kinetic energy")
ax4.plot(b1.t_t, b1.Eel_el, label = "Elastic energy")
ax4.plot(b1.t_t, b1.Etot_tot, label = "Total energy")
ax4.set_title("energy conservation")
ax4.set_xlabel("t $[s]$")
ax4.set_ylabel("E $[J]$")
plt.show()