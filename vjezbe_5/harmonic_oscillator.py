import math as m
import matplotlib.pyplot as plt

class HarmonicOscillator:


    def __init__(self, m, k, x0, v0, dt = 0.01):
        self.m = m
        self.k = k
        self.x0 = x0
        self.v0 = v0
        self.dt = dt
        self.t_t = []
        self.a_a = []
        self.x_x = []
        self.v_v = []


    def reset(self):
        self.a = 0.0
        self.x0 = 0.0
        self.v0 = 0.0
        self.t_t = []
        self.a_a = []
        self.x_x = []
        self.v_v = []


    def oscillate(self, T):
        t = 0.0
        while t < T:
            t += self.dt
            self.a = -(self.k / self.m) * self.x0
            self.v0 = self.v0 + self.a * self.dt
            self.x0 = self.x0 + self.v0 * self.dt
            self.a_a.append(self.a)
            self.v_v.append(self.v0)
            self.x_x.append(self.x0)
            self.t_t.append(t)


    def plot_trajectory(self):
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        fig.suptitle("Harmonic oscillator")

        ax1.plot(self.t_t, self.x_x)
        ax1.set_title("x-t graph")
        ax1.set_xlabel("t [s]")
        ax1.set_ylabel("x [m]") 

        ax2.plot(self.t_t, self.v_v)
        ax2.set_title("v-t graph")
        ax2.set_xlabel("t [s]")
        ax2.set_ylabel("v [m/s]") 

        ax3.plot(self.t_t, self.a_a)
        ax3.set_title("a-t graph")
        ax3.set_xlabel("t [s]")
        ax3.set_ylabel("a [m/$s^2$]")
        plt.show()


    def time_error(self, T):
        time = T
        A = self.x0
        alfa = m.sqrt(self.k / self.m)
        list_a = []
        list_v = []
        list_x = []
        list_t = []
        t = 0.0
        while t < T:
            a = - A * (alfa**2) * m.cos(alfa * t)
            v = - A * alfa * m.sin(alfa * t)
            x = A * m.cos(alfa * t)
            list_a.append(a)
            list_v.append(v)
            list_x.append(x)
            t += self.dt
            list_t.append(t)
        self.reset()
        self.a = float(list_a[0])
        self.x0 = float(list_x[0])
        self.v0 = float(list_v[0])
        self.oscillate(time)

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        fig.suptitle("Time error")

        ax1.plot(self.t_t, self.x_x)
        ax1.plot(list_t, list_x, ".")
        ax1.set_title("x-t graph")
        ax1.set_xlabel("t [s]")
        ax1.set_ylabel("x [m]")

        ax2.plot(self.t_t, self.v_v)
        ax2.plot(list_t, list_v, ".")
        ax2.set_title("v-t graph")
        ax2.set_xlabel("t [s]")
        ax2.set_ylabel("v [m/s]")

        ax3.plot(self.t_t, self.a_a)
        ax3.plot(list_t, list_a, ".")
        ax3.set_title("a-t graph")
        ax3.set_xlabel("t [s]")
        ax3.set_ylabel("a [m/$s^2$]")
        plt.show()


    def plot_trajectory2(self, T2, dt1, dt2):
        time2 = T2
        A2 = self.x0
        alfa = m.sqrt(self.k / self.m)
        list_x = []
        list_t = []
        list_x2 = []
        list_t2 = []
        list_x3 = []
        list_t3 = []
        t2 = 0.0
        while t2 < T2:
            x = A2 * m.cos(alfa * t2)
            list_x.append(x)
            t2 += self.dt
            list_t.append(t2)    
        self.reset()

        self.x0 = float(list_x[0])
        self.oscillate(time2)
        plt.plot(self.t_t, self.x_x, ".")
        self.dt = dt1
        self.reset()

        self.x0 = float(list_x[0])
        self.oscillate(time2)
        plt.plot(self.t_t, self.x_x, ".")
        self.dt = dt2
        self.reset()

        self.x0 = float(list_x[0])
        self.oscillate(time2)
        plt.plot(self.t_t, self.x_x, ".")
        plt.plot(list_t, list_x)
        plt.title("Time error")
        plt.xlabel("t [s]")
        plt.ylabel("x [m]")
        plt.show()