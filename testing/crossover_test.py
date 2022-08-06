from crossover import *


def test_single_point_crossover1():
    crossover = CrossoverMethod()
    crossover.config.GENOME_LENGTH = 4
    genotype_one = Genotype()
    genotype_one.genes = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0]]
    genotype_two = Genotype()
    genotype_two.genes = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 0]]
    offspring = crossover.single_point_crossover(genotype_one, genotype_two, crossover.generate_random_crossover_point())
    assert len(offspring) == 2
    assert len(offspring[0].genes) == 4
    assert len(offspring[1].genes) == 4


def test_single_point_crossover2():
    crossover = CrossoverMethod()
    crossover.config.GENOME_LENGTH = 6
    genotype_one = Genotype()
    genotype_one.genes = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
    genotype_two = Genotype()
    genotype_two.genes = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
    offspring = crossover.single_point_crossover(genotype_one, genotype_two, 2)
    assert len(offspring) == 2
    assert offspring[0].genes == [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
    assert offspring[1].genes == [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]


def test_double_point_crossover1():
    crossover = CrossoverMethod()
    crossover.config.GENOME_LENGTH = 6
    genotype_one = Genotype()
    genotype_one.genes = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
    genotype_two = Genotype()
    genotype_two.genes = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
    offspring = crossover.double_point_crossover(genotype_one, genotype_two, 1, 5)
    assert len(offspring) == 2
    assert len(offspring[0].genes) == 6
    assert len(offspring[1].genes) == 6


def test_double_point_crossover2():
    crossover = CrossoverMethod()
    crossover.config.GENOME_LENGTH = 6
    genotype_one = Genotype()
    genotype_one.genes = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
    genotype_two = Genotype()
    genotype_two.genes = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
    offspring = crossover.double_point_crossover(genotype_one, genotype_two, 2, 4)
    assert len(offspring) == 2
    assert offspring[0].genes == [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
    assert offspring[1].genes == [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]


def test_uniform_crossover():
    crossover = CrossoverMethod()
    crossover.config.GENOME_LENGTH = 6
    genotype_one = Genotype()
    genotype_one.genes = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
    genotype_two = Genotype()
    genotype_two.genes = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
    offspring = crossover.uniform_crossover(genotype_one, genotype_two)
    assert len(offspring) == 2
    assert len(offspring[0].genes) == 6
    assert len(offspring[1].genes) == 6
