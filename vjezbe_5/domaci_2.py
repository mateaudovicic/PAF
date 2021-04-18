import math as m
import matplotlib.pyplot as plt

class HarmonicOscillator:

    def __init__(self, m, k, x0, v0, k_el, S, dt = 0.01):
        self.m = m
        self.k = k
        self.x0 = x0
        self.v0 = v0
        self.dt = dt
        self.k_el = k_el
        self.S = S
        self.Cx = 0.47
        self.rho_air = 1.28
        self.t_t = []
        self.a_a = []
        self.x_x = []
        self.v_v = []

    def reset(self):
        self.m = 0.0
        self.k = 0.0
        self.x0 = 0.0
        self.v0 = 0.0
        self.dt = 0.0
        self.k_el = 0.0
        self.S = 0.0
        self.t_t.clear()
        self.a_a.clear()
        self.x_x.clear()
        self.v_v.clear()

    def oscillate1(self, T):
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

    def oscillate2(self, T):
        t = 0.0
        self.a = self.F / self.m
        while t < T:
            t += self.dt
            self.v0 = self.v0 + self.a * self.dt
            self.x0 = self.x0 + self.v0 * self.dt
            self.a_a.append(self.a)
            self.v_v.append(self.v0)
            self.x_x.append(self.x0)
            self.t_t.append(t)

    def gravity(self):
        Fg = self.m * 9.81
        return Fg

    def air_resistance(self):
        if self.x0 <= 0:
            Fot = self.Cx * self.S * ((self.rho_air * (self.v0)**2)/2)                                  
        else:
            Fot = - self.Cx * self.S * ((self.rho_air * (self.v0)**2)/2)
        return Fot

    def elastic_force(self):
        Fel = - self.k_el * self.x0
        return Fel

    def force_total(self, m):
        if m == 1:
            self.F = self.gravity()
            self.oscillate2(10)

        elif m == 2:
            self.F = self.air_resistance()
            self.oscillate2(10)

        elif m == 3:
            self.F = self.elastic_force()
            self.oscillate2(10)

        elif m == 12:
            self.F = self.gravity() + self.air_resistance()
            self.oscillate2(10)

        elif m == 13:
            self.F = self.gravity() + self.elastic_force()
            self.oscillate2(10)

        elif m == 23:
            self.F = self.air_resistance() + self.elastic_force()
            self.oscillate2(10)

        elif m == 123:
            self.F = self.gravity() + self.air_resistance() + self.elastic_force()
            self.oscillate2(10)

        else:
            self.F = - self.k / self.x0
            self.oscillate1(2)

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