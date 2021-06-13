import universe 
import numpy as np 
import matplotlib.pyplot as plt

au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun", "yellow", 1.989e30, np.array([0.,0.]), np.array([0.,0.]))
mercury = universe.Planet("Mercury", "darkorange", 3.3e24, np.array([0.,0.466 * au]), np.array([-47362.,0.]))
venus = universe.Planet("Venus", "red", 4.8685e24, np.array([0.723 * au, 0.]), np.array([0.,35020.]))
earth = universe.Planet("Earth", "blue", 5.9742e24, np.array([-1.*au,0.]), np.array([0.,-29783.]))
mars = universe.Planet("Mars", "brown", 6.417e23, np.array([0., -1.666 * au]), np.array([24007., 0.]))

ss = universe.Universe()
ss.add_planet(sun)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(earth)
ss.add_planet(mars)

ss.evolve(5.*year, day / 10)

img = plt.imread("yoda.jpg")
fig = plt.figure(figsize=(10,10))
plt.plot(sun.x_x, sun.y_y, label=sun.name, color=sun.color, linewidth=7.0)

plt.plot(mercury.x_x, mercury.y_y, label=mercury.name, color=mercury.color)
plt.plot(mercury.x_x[-1], mercury.y_y[-1], marker=".", markersize=20, color="orange")

plt.plot(venus.x_x, venus.y_y, label=venus.name, color=venus.color)
plt.plot(venus.x_x[-1], venus.y_y[-1], marker=".", markersize=20, color="orangered")

plt.plot(earth.x_x, earth.y_y, label=earth.name, color=earth.color)
plt.plot(earth.x_x[-1], earth.y_y[-1], marker=".", markersize=20, color="cyan")

plt.plot(mars.x_x, mars.y_y, label=mars.name, color=mars.color)
plt.plot(mars.x_x[-1], mars.y_y[-1], marker=".", markersize=20, color="goldenrod")

plt.imshow(img, extent=[min(mars.x_x), max(mars.x_x), min(mars.y_y), max(mars.y_y)])

plt.xlabel("x")
plt.ylabel("y")
plt.title("$Solar$ $system$")
plt.legend(loc="upper right")
plt.show()