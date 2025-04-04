# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

import genotype

from config import *


class InitialGeneration(Config):
    def __init__(self):
        super().__init__()

    def initialise(self):
        """
        Method to create the initial population for the algorithm.
        :return: a 3D array
        """
        population = [[0] * self.GENOME_LENGTH for i in [1] * self.POPULATION]
        for individual in range(self.POPULATION):
            population[individual] = genotype.Genotype()
        return population
