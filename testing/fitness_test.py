from fitness import *


def test_evaluate_fitness1():
    optimal_genotype = Genotype()
    optimal_genotype.genes = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]]
    individual_genotype = Genotype()
    individual_genotype.genes = [[0, 1, 0, 1], [0, 0, 0, 1], [1, 0, 1, 1], [0, 0, 1, 0]]
    fitness = Fitness()
    fitness.config.GENOME_LENGTH = 4
    fitness.fitness = 16
    fitness.evaluate_fitness(optimal_genotype, individual_genotype)
    assert individual_genotype.fitness == 5
