import matplotlib.pyplot as plt
import harmonic_oscillator as ho

list_dt = []
list_err = []
dt = 0.0
N = 100

for i in range(N):
    dt += 0.01
    list_dt.append(dt)
    h1 = ho.HarmonicOscillator(0.1, 10, 0.3, 0, dt)
    error = abs(h1.numeric() - h1.analytic()) / h1.numeric() *100
    list_err.append(error)

plt.plot(list_dt, list_err)
plt.ylabel("absolute relative error [%]")
plt.xlabel("dt [s]")
plt.title("Absolute relative error")
plt.show()