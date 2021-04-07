import math as m
import numpy as np
import matplotlib.pyplot as plt

# Kubna i trigonometrijska funkcija

def f1(x):
    return x*x-2*x

def f2(x):
    return m.sin(x)


# Funkcija za deriviranje

def f3(x):
    return 5*x**3 - 2*x**2 + 2*x - 3

def f33( x):
    return 15*x**2 - 4*x + 2


# Funkcija za integriranje

def f4(x):
    return 2*x**2 + 3

def f44(x):
    return 2*(x**3/3) + 3*x


# Deriviranje

def deriv_3(func, x, h):
    d3 = ((func(x + h)) - (func(x - h))) / (2*h)
    return d3 

def deriv_2(func, x, h):
    d2 = ((func(x)) - (func(x - h))) / h
    return d2
    
def der(func, x1, x2, h, m):
    list_x = np.arange(x1, x2, h)
    list_d = []
    if m == 3:
        for x in list_x:
            d = deriv_3(func, x, h)
            list_d.append(d)
    elif m==2:
        for x in list_x:
            d = deriv_2(func, x, h)
            list_d.append(d)
    return list_x, list_d


# Integriranje

def integral(func, a, b, N):
    dx = (b-a) / N
    g_x = a + dx
    d_x = a
    g_m = 0.0
    d_m = 0.0
    for i in range(N):
        if abs(func(g_x)) >= abs(func(d_x)):
            g_m += func(g_x)*dx        
            d_m += func(d_x)*dx
        else:
            g_m += func(d_x)*dx        
            d_m += func(g_x)*dx
        g_x += dx
        d_x += dx
    return g_m, d_m

def trapezium(func, a, b, N):
    dx = (b-a) / N
    g_x = a + dx
    d_x = a
    I = 0.0
    for i in range(N):
        I += ((func(g_x) + func(d_x)) /2) *dx
        g_x += dx
        d_x += dx 
    return I

def analytic(func, x1, x2):
    a = func(x2) - func(x1)
    return a