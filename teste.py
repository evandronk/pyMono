import pyMono as Mono

data = Mono.load('iso1.csv', p0=1, nist_csv=True)


resultado = Mono.estimate(data.p, data.q, 'sips')
resultado.plot()

resultado.kruskal()
