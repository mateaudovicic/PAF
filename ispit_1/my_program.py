import bullet as bll 
import matplotlib.pyplot as plt 


# zadatak_1

b0 = bll.Bullet()
b0.init(30, 20)
b0.reset()
print("")


# zadatak_2

b1 = bll.Bullet()
b1.init(30, 20)
b1.change_height(-5)
b1.change_speed(-5)
b1.reset()

print("")

b2 = bll.Bullet()
b2.init(40, 30)
b2.change_height(5)
b2.change_speed(5)
b2.reset()
print("")


# zadatak_3

b3 = bll.Bullet()
b3.init(2, 100)
b3.plot_trajectory()
b3.reset()


# zadatak_4

plt.vlines(x=50, ymin=1.4, ymax=1.6, colors='green', lw=2)

b4 = bll.Bullet()
b4.init(2, 0)
b4.velocity_to_hit_target(50, 1.5, 1.4, 1.6, 0.01) 
print("Brzina za dt = 0.01 s: {}".format(b4.v0))

plt.plot(b4.x_x, b4.y_y)

b4.reset()

b4 = bll.Bullet()
b4.init(2, 0)
b4.velocity_to_hit_target(50, 1.5, 1.4, 1.6, 0.05)  
print("Brzina za dt = 0.05 s: {}".format(b4.v0))
b4.reset()

b4 = bll.Bullet()
b4.init(2, 0)
b4.velocity_to_hit_target(50, 1.5, 1.4, 1.6, 0.1) 
print("Brzina za dt = 0.1 s: {}".format(b4.v0))
b4.reset()


# zadatak_5

plt.vlines(x=50, ymin=1.4, ymax=1.6, colors='green', lw=2)

b5 = bll.Bullet()
b5.init(2, 0)
b5.velocity_to_hit_target(50, 1.5, 1.4, 1.6, 0.05)
plt.plot(b5.x_x, b5.y_y)
b5.reset()

b5 = bll.Bullet()
b5.init(2, 0)
b5.air_resistance(50, 1.5, 1.4, 1.6, 0.05, 0.1, 2)
plt.plot(b5.x_x, b5.y_y)
plt.show()