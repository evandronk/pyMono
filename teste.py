import load
import mono_pso
import mono_iso


data = load.load('iso.csv', nist_csv=True)
print(data.p)
print(data.q)

mono_pso.pso(data.p, data.q, mono_iso.langmuir)


