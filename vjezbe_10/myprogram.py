import Particle as prt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

p0 = prt.el_magn_field()
p1 = prt.el_magn_field()

# 1. zadatak

p0.init(1, -1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))  
p0.move_eu(15)
p1.init(1, 1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))  
p1.move_eu(15)

ax = plt.axes(projection = "3d")
ax.plot3D(p0.x_x, p0.y_y, p0.z_z, label = "electron $(q = -1,  m = 1)$")
ax.plot3D(p1.x_x, p1.y_y, p1.z_z, label = "positron $(q = 1,  m = 1)$")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Electromagnetic filed")
ax.view_init(30, 30)
plt.legend()
plt.show()

# 2. zadatak

p2 = prt.el_magn_field()
p2.init(1, -1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))
p2.move_rk(15)

ax = plt.axes(projection = "3d")
ax.plot3D(p0.x_x, p0.y_y, p0.z_z, label = "Euler's method")
ax.plot3D(p2.x_x1, p2.y_y1, p2.z_z1, label = "Runge-Kutta method")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Electron")
ax.view_init(30, 30)
plt.legend()
plt.show()