import pyMono as Mono

data = Mono.load('iso1.csv', p0=1, nist_csv=True)


resultado = Mono.estimate(data.p, data.q, 'teste')
resultado.plot()

resultado.kruskal()
resultado.error_all() 