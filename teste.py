import load
import mono_pso
import mono_iso
import simulated_iso


data = load.load('artigo5.csv', p0=65, nist_csv=True)
print(data.p)
print(data.q)

resultado = mono_pso.pso(data.p, data.q, mono_iso.modified_bet)
print(resultado)

load.plot(data)
sim_data = simulated_iso.create(data.p, resultado[0], mono_iso.__modified_bet_q__)
load.plot(sim_data)