import pyMono as Mono

data = Mono.load('iso1.csv', p0=1, nist_csv=True)
data.plot()
print(data.p)
print(data.q)

resultado = Mono.estimate(data.p, data.q, 'multisite')
resultado.plot()
resultado.plot_exp()
resultado.plot_sim()

resultado.error_all()
