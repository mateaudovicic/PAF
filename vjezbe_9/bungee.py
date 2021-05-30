import math as m

class BungeeJumping:


    def init(self, mass, k, h0, l, v0, S, dt = 0.001, Cx = 0.47, rho_air = 1.28):
        self.mass = mass
        self.k = k
        self.h0 = h0
        self.y = h0
        self.l = l
        self.v0 = v0
        self.S = S
        self.Cx = Cx
        self.rho_air = rho_air
        self.dt = dt
        self.g = 9.81
        self.a = 0.0
        self.d = 0.0
        self.t = 0.0
        self.Ep = 0.0
        self.Ek = 0.0
        self.Eel = 0.0
        self.Etot = 0.0
        self.Ep_p = []
        self.Ek_k = []
        self.Eel_el = []
        self.Etot_tot = []
        self.t_t = []
        self.y_y = []

    
    def reset(self):
        self.mass = 0.0
        self.k = 0.0
        self.h0 = 0.0
        self.y = 0.0
        self.l = 0.0
        self.v0 = 0.0
        self.S = 0.0
        self.dt = 0.0
        self.Cx = 0.0
        self.rho_air = 0.0
        self.a = 0.0
        self.d = 0.0
        self.t = 0.0
        self.Ep = 0.0
        self.Ek = 0.0
        self.Eel = 0.0
        self.Etot = 0.0
        self.t_t.clear()
        self.y_y.clear()
        self.Ep_p.clear()
        self.Ek_k.clear()
        self.Eel_el.clear()
        self.Etot_tot.clear()


    def __potential_energy(self, d):
        return (self.g * self.mass * d)


    def __kinetic_energy(self):
        return (self.mass * (self.v0**2)) / 2


    def __elastic_energy(self, d):
        if d > 0.0:
            Eel = (self.k * (d**2)) / 2
        else:
            Eel = 0.0
        return Eel


    def __total_energy(self):
        return (self.Ep + self.Ek + self.Eel)


    def __acceleration(self, d, v0):   
        if d > 0.0:
            a_el = (self.k/self.mass) * d
        else:
            a_el = 0.0
        if v0 > 0.0:
            a_ar = - abs((v0**2) * self.rho_air * self.Cx * self.S) / (2*self.mass)
        else:
            a_ar = abs((v0**2) * self.rho_air * self.Cx * self.S) / (2*self.mass)
        return (-self.g + a_el + a_ar)


    def move(self, T):
        while self.t <= T:
            self.d = self.h0 - self.l - self.y
            self.a = self.__acceleration(self.d, self.v0)  
            self.v0 += self.a * self.dt
            self.y += self.v0 * self.dt

            self.t += self.dt
            self.y_y.append(self.y)
            self.t_t.append(self.t)

            self.Ep = self.__potential_energy(self.y)
            self.Ek = self.__kinetic_energy()
            self.Eel = self.__elastic_energy(self.d)
            self.Ep_p.append(self.Ep)
            self.Ek_k.append(self.Ek)
            self.Eel_el.append(self.Eel)
            self.Etot = self.__total_energy()
            self.Etot_tot.append(self.Etot) 