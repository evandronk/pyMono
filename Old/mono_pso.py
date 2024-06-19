import random
import numpy as np


class Particle:
    def __init__(self, param):
        self.position = np.array(
            [min_max[0] + random.random() * (min_max[1] - min_max[0]) for min_max in param])
        self.velocity = np.zeros_like(self.position)
        self.best_position = self.position.copy()
        self.best_fitness = float('inf')
        self.fitness = float('inf')


def velocity(particle, swarm_best_position):
    w = 0.8
    c1 = 1.2
    c2 = 1.2
    r1 = random.random()
    r2 = random.random()
    v = particle.velocity
    best_position = particle.best_position
    position = particle.position
    return w * v + c1 * r1 * (best_position - position) + c2 * r2 * (swarm_best_position - position)


def pso(p, qe, obj_func, part_n=100, iter_n=100, param=[[0.1, 10], [1, 100], [0.1, 10]], comp_n=1, relative=False):

    if param is None:
        param = [[0.1, 10], [1, 100], [0.1, 10]]
    particles_list = []
    swarm_best_fitness = float('inf')
    swarm_best_position = [1, 1, 1]
    print(param)
    for _ in range(part_n):
        for _ in range(comp_n):
            particle = Particle(param)
            fitness = obj_func(p, qe, particle.position, relative)
            particle.fitness = fitness
            particle.best_position = particle.position.copy()
            particle.best_fitness = fitness
            particles_list.append(particle)
            if _ == 0:
                swarm_best_fitness = fitness
                swarm_best_position = particle.position.copy()
            if fitness < swarm_best_fitness:
                swarm_best_fitness = fitness
                swarm_best_position = particle.position.copy()

    for _ in range(iter_n):
        for particle in particles_list:
            v = velocity(particle, swarm_best_position)
            particle.velocity = v
            particle.position += v
            fitness = obj_func(p, qe, particle.position, relative)
            particle.fitness = fitness
            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position.copy()
            if fitness < swarm_best_fitness:
                swarm_best_fitness = fitness
                swarm_best_position = particle.position.copy()

    return swarm_best_position, swarm_best_fitness
