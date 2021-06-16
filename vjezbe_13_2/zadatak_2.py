from matplotlib import pyplot as plt
import math as m
import numpy as np
from matplotlib.animation import FuncAnimation 
import universe 

au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun", "yellow", 1.989e30, 0.696*1e9, np.array([0.,0.]), np.array([0.,0.]), )
mercury = universe.Planet("Mercury", "darkorange", 3.3e24, 2.439*1e6, np.array([0.,0.466 * au]), np.array([-47362.,0.]))
venus = universe.Planet("Venus", "red", 4.8685e24, 6.051*1e6, np.array([0.723 * au, 0.]), np.array([0.,35020.]))
earth = universe.Planet("Earth", "blue", 5.9742e24, 6.371*1e6, np.array([-1.*au,0.]), np.array([0.,-29783.]))
mars = universe.Planet("Mars", "brown", 6.417e23, 3.389*1e6, np.array([0., -1.666 * au]), np.array([24007., 0.]))

ss = universe.Universe()

planets = [sun, mercury, venus, earth, mars]
c_comets = []

fig = plt.figure()  
axis = plt.axes() 

for c in range(5):
    mass = np.random.uniform(1.0, 9.9e13)
    radius = np.random.uniform(0.1, 0.5e3)
    position_x = np.random.uniform(1.600e11, 4*1.496e11)
    position_y = np.random.uniform(0.0, 0.0)
    velocity_x = np.random.uniform(-1.0e4, -4e4)
    velocity_y = np.random.uniform(-1.0e4, -4e4)
    comet = universe.Planet("comet", "black", mass, radius, np.array([position_x, position_y]), np.array([velocity_x, velocity_y]))
    axis.plot(comet.x_x, comet.y_y, label=comet.name, color=comet.color)
    c_comets.append(comet)
    ss.add_planet(comet)
    planets.append(comet)

    ss.add_planet(sun)
    ss.add_planet(mercury)
    ss.add_planet(venus)
    ss.add_planet(earth)
    ss.add_planet(mars)


    d = ss.evolve(5.*year, day / 10)


    lines = []

    axis.plot(sun.x_x, sun.y_y, label=sun.name, color=sun.color, linewidth=7.0)
    axis.plot(mercury.x_x, mercury.y_y, label=mercury.name, color=mercury.color)
    axis.plot(venus.x_x, venus.y_y, label=venus.name, color=venus.color)
    axis.plot(earth.x_x, earth.y_y, label=earth.name, color=earth.color)
    axis.plot(mars.x_x, mars.y_y, label=mars.name, color=mars.color)
        
    for p in planets:
        line = axis.plot([], [], "o", color=p.color)[0]
        lines.append(line) 
        

    def init(): 
        for line in lines:
            line.set_data([], [])
        return lines


    def animate(i):
        for index, p in enumerate(planets):
            x = p.x_x[i]   
            y = p.y_y[i]   
            lines[index].set_data(x, y)      
        return lines


    anim = FuncAnimation(fig, animate, init_func = init,
                        frames = 3000, interval = 1, blit = True)


    plt.show()