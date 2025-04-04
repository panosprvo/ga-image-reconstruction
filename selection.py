# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

import numpy.random as npr

from config import Config


class Selection(Config):

    def __init__(self):
        super().__init__()

    def roulette_selection(self, population):
        """
        For the selection operator we are using the roulette-wheel operator (read README for more information). This
        method is selecting an individual from the population that will be used to create offspring for the next
        generation.

        :return: Genotype object.
        """
        cumulative_fitness = sum(individual.fitness for individual in population)
        selection_probability = [individual.fitness/cumulative_fitness for individual in population]
        return population[npr.choice(len(population), p=selection_probability)]
