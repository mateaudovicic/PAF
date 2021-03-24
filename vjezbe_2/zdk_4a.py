import matplotlib.pyplot as plt
import numpy as np
import math as m
from zdk_4b import graf,v_max, h_max, domet, meta_putanja, udaljenost

v0 = 30
g = 9.81
alfa = (np.pi/4)

p = 20
q = 20
r = 5
        
graf(v0, alfa, g, p, r, q)
h_max(v0, g, alfa)
v_max(v0, alfa, g)
meta_putanja(p, q, r, v0, alfa, g)
udaljenost(r, v0, alfa, p, q, g)
domet(v0, g, alfa)
