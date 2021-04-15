import harmonic_oscillator as ho

h1 = ho.HarmonicOscillator(0.1, 10, 0.3, 0)
h1.oscillate(2)
h1.plot_trajectory()
h1.time_error(3)
h1.plot_trajectory2(2, 0.001, 0.05)
h1.numeric()
h1.analytic()

# domaći 2

"""import domaci_2 as do
d1 = do.HarmonicOscillator(0.1, 10, 0.3, 0, 0.5, 0.5)
d1.force(123)
d1.plot_trajectory()"""