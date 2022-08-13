# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

import random

from config import Config


class Genotype:

    def __init__(self):
        self.config = Config()
        self.genes = [[random.randint(0, 1) for i in range(0, self.config.GENOME_LENGTH)]
                      for i in range(0, self.config.GENOME_LENGTH)]
        self.fitness = 0

    def mutation(self):
        """
        Depending on config.MUTATION_PROBABILITY, we produce a random number between 0 and 1 to decide whether a
        mutation for the specific gene should take place or not. Mutation is the reversal of 0 to 1, and 1 to 0.
        :return: void - method that only flips genes that should be mutated.
        """
        for j in range(self.config.GENOME_LENGTH):
            for index in range(self.config.GENOME_LENGTH):
                if random.uniform(0, 1) <= self.config.MUTATION_PROBABILITY:
                    self.genes[j][index] = self.__mutate__(self.genes[j][index])

    def __mutate__(self, gene):
        if gene == 0:
            return 1
        return 0
