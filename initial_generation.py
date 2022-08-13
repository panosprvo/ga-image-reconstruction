# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

import genotype

from config import *


class InitialGeneration:
    def __init__(self):
        self.config = Config()

    def initialise(self):
        """
        Method to create the initial population for the algorithm.
        :return: a 3D array
        """
        population = [[0] * self.config.GENOME_LENGTH for i in [1] * self.config.POPULATION]
        for individual in range(self.config.POPULATION):
            population[individual] = genotype.Genotype()
        return population
