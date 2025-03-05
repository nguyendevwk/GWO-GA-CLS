

import numpy as np


class GeneticAlgorithm:
    def __init__(self, dim, popSize, Iter, lb, ub, mutation_rate, crossover_rate, fitness_func):
        self.dim = dim
        self.popSize = popSize
        self.Iter = Iter
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.fitness_func = fitness_func
        self.lb = lb
        self.ub = ub

    def initialize_population(self):
        min_val, max_val = self.lb, self.ub
        return np.random.uniform(min_val, max_val, size=(self.popSize, self.dim))

    def calculate_fitness(self, population):
        return np.array([self.fitness_func(individual) for individual in population])

    def selection(self, population, fitness_scores):
            # Sort the population based on fitness scores in ascending order
            sorted_indices = np.argsort(fitness_scores)
            sorted_population = population[sorted_indices]
            return sorted_population[:self.popSize]

    def crossover(self, parents):
        offspring = np.empty((self.popSize, self.dim))
        for i in range(0, self.popSize, 2):
            parent1_idx = i % len(parents)
            parent2_idx = (i + 1) % len(parents)
            parent1 = parents[parent1_idx]
            parent2 = parents[parent2_idx]

            crossover_point = np.random.randint(1, self.dim - 1) if self.dim >= 3 else 1

            offspring[i, 0:crossover_point] = parent1[0:crossover_point]
            offspring[i, crossover_point:] = parent2[crossover_point:]
            offspring[i + 1, 0:crossover_point] = parent2[0:crossover_point]
            offspring[i + 1, crossover_point:] = parent1[crossover_point:]

        return offspring

    def mutate(self, population):
        for i in range(self.popSize):
            for j in range(self.dim):
                if np.random.rand() < self.mutation_rate:
                    min_val = max(self.lb, population[i][j] - 0.1 * abs(self.lb))
                    max_val = min(self.ub, population[i][j] + 0.1 * abs(self.ub))
                    population[i][j] = np.random.uniform(min_val, max_val)
        return population

    def optimize(self):
        population = self.initialize_population()
        fitness_history = []
        array_fitness = []

        for iteration in range(self.Iter):
            fitness_scores = self.calculate_fitness(population)

            parents = self.selection(population, fitness_scores)
            children = self.crossover(parents)
            population_new = self.mutate(children)

            population = np.vstack((population, population_new))
            # Selection is now after crossover and mutation
            fitness_scores = self.calculate_fitness(population)
            sorted_indices = np.argsort(fitness_scores)
            population = population[sorted_indices[:self.popSize]]
            fitness_history.append(np.min(fitness_scores))

            if iteration % 100 == 0:
                array_fitness.append(np.min(fitness_history))

        return fitness_history, array_fitness
