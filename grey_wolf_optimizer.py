

import numpy as np

class GWO:
    def __init__(self, dim, popSize, Iter, lb, ub, fitness_func):
        self.dim = dim
        self.popSize = popSize
        self.Iter = Iter
        self.lb = lb
        self.ub = ub
        # self.search_space = search_space
        self.fitness_func = fitness_func

    def initialize_population(self):
        return np.random.uniform(self.lb, self.ub, size=(self.popSize, self.dim))

    def calculate_fitness(self, wolves):
        fitness = np.zeros(self.popSize)
        for i, wolf in enumerate(wolves):
            fitness[i] = self.fitness_func(wolf)
        return fitness

    def optimize(self):
        wolves = self.initialize_population()
        fitness_history = []
        array_fitness = []
        for iteration  in range(self.Iter):
            fitness = self.calculate_fitness(wolves)
            alpha_index = np.argmin(fitness)
            beta_index = np.argsort(fitness)[1]
            delta_index = np.argsort(fitness)[2]

            alpha, beta, delta = wolves[alpha_index], wolves[beta_index], wolves[delta_index]

            a = 2 - 2 * (iteration  / self.Iter)  # linearly decreased from 2 to 0

            new_wolves = np.zeros_like(wolves)

            for i in range(self.popSize):
                r1 = np.random.random(self.dim)
                r2 = np.random.random(self.dim)

                A1 = 2 * a * r1 - a
                C1 = 2 * r2

                D_alpha = abs(C1 * alpha - wolves[i])
                X1 = alpha - A1 * D_alpha

                r1 = np.random.random(self.dim)
                r2 = np.random.random(self.dim)

                A2 = 2 * a * r1 - a
                C2 = 2 * r2

                D_beta = abs(C2 * beta - wolves[i])
                X2 = beta - A2 * D_beta

                r1 = np.random.random(self.dim)
                r2 = np.random.random(self.dim)

                A3 = 2 * a * r1 - a
                C3 = 2 * r2

                D_delta = abs(C3 * delta - wolves[i])
                X3 = delta - A3 * D_delta

                wolves_new = (X1 + X2 + X3) / 3
                # new_wolves[i] = wolves_new

                if self.fitness_func(wolves_new) < self.fitness_func(wolves[i]):
                    new_wolves[i] = wolves_new
                else:
                    new_wolves[i] = wolves[i]

            wolves = new_wolves

            fitness_history.append(np.min(fitness))
            if iteration % 100 == 0:
                array_fitness.append(np.min(fitness_history))

        return fitness_history, array_fitness



