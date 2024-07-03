import pyMono as Mono

data = Mono.load('30.csv', p0=1, nist_csv=True)

#

#data2 = Mono.Isotherm([2.1,0.7], 8)

resultado = Mono.estimate(data.p, data.q, 'toth')


resultado.plot(export=True)



