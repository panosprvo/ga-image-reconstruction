# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------
import config
from initial_generation import *


def test_population_generation1():
    pop_gen = InitialGeneration()
    population = pop_gen.initialise()
    assert len(population) == config.Config().POPULATION
    assert len(population[0].genes) == config.Config().GENOME_LENGTH
    assert len(population[0].genes[0]) == config.Config().GENOME_LENGTH
