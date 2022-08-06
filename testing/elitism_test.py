from elitism import Elitism
from population_generation import InitialGeneration


def test_find_elites1():
    elit = Elitism()
    elit.config.ELITE_CARRY_OVER = 2
    init_population = InitialGeneration()
    init_population.config.POPULATION = 4
    population = init_population.initialise()

    population[0].genes = [[1, 1, 0], [0, 1, 0], [0, 0, 0]]
    population[1].genes = [[1, 1, 1], [1, 0, 1], [0, 0, 1]]
    population[2].genes = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    population[3].genes = [[0, 0, 1], [1, 0, 1], [0, 1, 1]]

    population[0].fitness = 1
    population[1].fitness = 2
    population[2].fitness = 4
    population[3].fitness = 7
    elites = elit.find_elites(population)

    assert elites[0].genes == [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    assert elites[1].genes == [[0, 0, 1], [1, 0, 1], [0, 1, 1]]


def test_find_elites2():
    elit = Elitism()
    elit.config.ELITE_CARRY_OVER = 2
    init_population = InitialGeneration()
    init_population.config.POPULATION = 4
    population = init_population.initialise()

    population[0].genes = [[1, 1, 0], [0, 1, 0], [0, 0, 0]]
    population[1].genes = [[1, 1, 1], [1, 0, 1], [0, 0, 1]]
    population[2].genes = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    population[3].genes = [[0, 0, 1], [1, 0, 1], [0, 1, 1]]

    population[0].fitness = 7
    population[1].fitness = 2
    population[2].fitness = 7
    population[3].fitness = 7
    elites = elit.find_elites(population)

    assert elites[0].genes == [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    assert elites[1].genes == [[0, 0, 1], [1, 0, 1], [0, 1, 1]]
