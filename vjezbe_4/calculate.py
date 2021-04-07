import math as m
import calculus
import matplotlib.pyplot as plt

h = 0.1


# Derivacija kubne i trigonometrijske funkcije

print(calculus.deriv_3(calculus.f1, 2, h))
print(calculus.deriv_2(calculus.f1, 2, h))
print(calculus.deriv_3(calculus.f2, 2, h))
print(calculus.deriv_2(calculus.f2, 2, h))


# Deriviranje - graf

lista1, lista2 = calculus.der(calculus.f3, -2, 2, h, 3)
plt.plot(lista1, lista2, ".")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.title("Numerical derivation $f(x) = 5x^3 - 2x^2 + 2x - 3$")

lista1_1, lista2_2 = calculus.der(calculus.f3, -2, 2, 0.2, 3)
plt.plot(lista1_1, lista2_2, ".") 

d = -2
g = 2
lista3 = lista1.copy()
lista4 = []
while d < g:
    y = calculus.f33(d)
    lista4.append(y)
    d += h
plt.plot(lista3,lista4)
plt.show()


# Integriranje

gornja, donja = calculus.integral(calculus.f4, 0, 1, 1000)
print("Gornja i donja međa: {} ; {}".format(gornja, donja))
result = calculus.trapezium(calculus.f4, 0, 1, 1000)
print("Rješenje integrala: {}".format(result))

analyt = calculus.analytic(calculus.f44, 0, 1)
plt.axhline(y=analyt)

x_x = []
g_y = []
d_y = []
dots = []
x = 0
for i in range(20):
    x += 50
    x_x.append(x)
    gornja, donja = calculus.integral(calculus.f4, 0, 1, x)
    result = calculus.trapezium(calculus.f4, 0, 1, x)
    g_y.append(gornja)
    d_y.append(donja)
    dots.append(result)
plt.plot(x_x, g_y, ".")
plt.plot(x_x, d_y, ".")
plt.plot(x_x, dots, ".")
plt.ylabel('Integral')
plt.xlabel('N steps')
plt.title("Numerical integration $f(x) = 5x^3 - 2x^2 + 2x - 3$")
plt.show()