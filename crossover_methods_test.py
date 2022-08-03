import numpy

from crossover_methods import *


def test_single_point_crossover1():
    crossover = CrossoverMethod()
    crossover.config.GENOME_LENGTH = 4
    genome_one = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0]]
    genome_two = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 0]]
    offspring = crossover.single_point_crossover(genome_one, genome_two, crossover.generate_random_crossover_point())
    assert len(offspring) == 2
    assert len(offspring[0]) == 4
    assert len(offspring[1]) == 4


def test_single_point_crossover2():
    crossover = CrossoverMethod()
    crossover.config.GENOME_LENGTH = 6
    genome_one = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
    genome_two = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
    offspring = crossover.single_point_crossover(genome_one, genome_two, 2)
    assert len(offspring) == 2
    assert numpy.array_equal(
        offspring[0], [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]])
    assert numpy.array_equal(
        offspring[1], [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]])


def test_double_point_crossover1():
    crossover = CrossoverMethod()
    crossover.config.GENOME_LENGTH = 6
    genome_one = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
    genome_two = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
    offspring = crossover.double_point_crossover(genome_one, genome_two, 1, 5)
    assert len(offspring) == 2
    assert len(offspring[0]) == 6
    assert len(offspring[1]) == 6


def test_double_point_crossover2():
    crossover = CrossoverMethod()
    crossover.config.GENOME_LENGTH = 6
    genome_one = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
    genome_two = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
    offspring = crossover.double_point_crossover(genome_one, genome_two, 2, 4)
    assert len(offspring) == 2
    assert numpy.array_equal(
        offspring[0], [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]])
    assert numpy.array_equal(
        offspring[1], [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]])


def test_uniform_crossover():
    crossover = CrossoverMethod()
    crossover.config.GENOME_LENGTH = 6
    genome_one = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
    genome_two = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
    offspring = crossover.uniform_crossover(genome_one, genome_two)
    assert len(offspring) == 2
    assert len(offspring[0]) == 6
    assert len(offspring[1]) == 6
