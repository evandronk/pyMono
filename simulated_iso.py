import load


def create(p, param, model):
    q_sim = []
    for press in p:
        q_sim.append(model(press, param))
    return load.Isotherm(p, q_sim)
