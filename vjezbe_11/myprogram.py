import matplotlib.pyplot as plt
import solar_system as ss 
import numpy as np 

mS = 1.989 * (10**30)
mE =  5.9742 * (10**24)
rS = np.array([0, 0])
rE = np.array([1.486 * (10**11), 0])
vS = np.array([0, 0])
vE = np.array([0, 29783])

s0 = ss.Solar_System()
s0.init(mS, mE, rS, rE, vS, vE)
s0.move(60*60*24*365.242)

plt.figure("Solar system")
plt.plot(s0.x_x1, s0.y_y1, color = 'yellow', label = "The sun", linewidth = 4)
plt.plot(s0.x_x2, s0.y_y2, color = 'blue', label = "The earth")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()