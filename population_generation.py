import random

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
            for gene in range(self.config.GENOME_LENGTH):
                population[individual][gene] = [random.randint(0, 1) for i in range(0, self.config.GENOME_LENGTH)]
        return population


def main():
    pop = InitialGeneration()
    population = pop.initialise()
    print(population)


if __name__ == '__main__':
    main()
