from population_generation import *


def test_population_generation1():
    pop_gen = InitialGeneration()
    pop_gen.config.POPULATION = 5
    pop_gen.config.GENOME_LENGTH = 4
    population = pop_gen.initialise()
    assert len(population) == 5
    assert len(population[0]) == 4
    assert len(population[0][0]) == 4
