from fitness import *


def test_evaluate_fitness1():
    optimal_array = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]]
    individual_array = [[0, 1, 0, 1], [0, 0, 0, 1], [1, 0, 1, 1], [0, 0, 1, 0]]
    fitness = Fitness()
    fitness.config.GENOME_LENGTH = 4
    fitness.fitness = 16
    individual_fitness = fitness.evaluate_fitness(optimal_array, individual_array)
    assert individual_fitness == 5
