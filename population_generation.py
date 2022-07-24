import random

from config import Config


class InitialGeneration:

    def __init__(self):
        self.config = Config()
        self.population = [[0] * self.config.GENOME_LENGTH for i in [1] * self.config.POPULATION]

    def initialise(self):
        """

        :return:
        """
        for individual in range(self.config.POPULATION):
            for gene in range(self.config.GENOME_LENGTH):
                self.population[individual][gene] = [random.randint(0, 1) for i in range(0, self.config.GENOME_LENGTH)]


def main():
    return


if __name__ == '__main__':
    main()
