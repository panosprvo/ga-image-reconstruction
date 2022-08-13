# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

from fitness import *


def test_evaluate_fitness():
    optimal_genotype = Genotype()
    optimal_genotype.genes = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]]
    individual_genotype = Genotype()
    individual_genotype.genes = [[0, 1, 0, 1], [0, 0, 0, 1], [1, 0, 1, 1], [0, 0, 1, 0]]
    fitness = Fitness()
    fitness.config.GENOME_LENGTH = 4
    fitness.fitness_to_reach = 16
    fitness.evaluate_fitness(optimal_genotype, individual_genotype)
    assert individual_genotype.fitness == 5


def test_get_max_fitness():
    gen1 = Genotype()
    gen1.genes = [[0, 0, 0], [0, 0, 1], [1, 0, 1]]
    gen1.fitness = 10
    gen2 = Genotype()
    gen2.genes = [[0, 0, 0], [0, 0, 1], [1, 0, 1]]
    gen2.fitness = 15
    gen3 = Genotype()
    gen3.genes = [[0, 0, 0], [0, 0, 1], [1, 0, 1]]
    gen3.fitness = 25
    population = [gen1, gen2, gen3]

    fitness = Fitness()
    fitness.config.GENOME_LENGTH = 3
    assert fitness.get_max_fitness(population) == 25


def test_max_fitness_genotype():
    gen1 = Genotype()
    gen1.genes = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
    gen1.fitness = 10
    gen2 = Genotype()
    gen2.genes = [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
    gen2.fitness = 15
    gen3 = Genotype()
    gen3.genes = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    gen3.fitness = 25
    population = [gen1, gen2, gen3]

    fitness = Fitness()
    fitness.config.GENOME_LENGTH = 3
    test_gen = fitness.max_fitness_genotype(population)
    assert test_gen.genes == gen3.genes
