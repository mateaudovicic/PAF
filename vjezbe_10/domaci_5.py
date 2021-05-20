import Particle as prt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# ružno izgleda za T = 10 sekundi pa sam stavila T = 20 sekundi

p0 = prt.el_magn_field()
p1 = prt.el_magn_field()

p0.init(1, -1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))  
p0.move_eu(20)

p1.init(1, -1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))  
p1.move_eu2(20)

# 1. zadatak (putanja elektrona u konstantnom i vremenski promjenjivom magnetskom polju)

ax = plt.axes(projection = "3d")
ax.plot3D(p0.x_x, p0.y_y, p0.z_z, label = "constant")
ax.plot3D(p1.x_x2, p1.y_y2, p1.z_z2, label = "time changeable")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Electromagnetic filed")
ax.view_init(30, 30)
plt.legend()
plt.show()

p0.reset()
p1.reset()

# 2. zadatak (putanje elektrona i pozitrona u vremenski promjenjivom magnetskom polju)

p2 = prt.el_magn_field()
p3 = prt.el_magn_field()

p2.init(1, -1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))
p2.move_eu2(20)

p3.init(1, 1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))  
p3.move_eu2(20)

ax = plt.axes(projection = "3d")
ax.plot3D(p2.x_x2, p2.y_y2, p2.z_z2, label = "electrone")
ax.plot3D(p3.x_x2, p3.y_y2, p3.z_z2, label = "positron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Electromagnetic filed")
ax.view_init(30, 30)
plt.legend()
plt.show()