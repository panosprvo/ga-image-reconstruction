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
        for index in range(self.config.POPULATION):
            self.population[index] = [random.randint(0, 1) for i in range(0, self.config.GENOME_LENGTH)]


def main():
    pop = InitialGeneration()
    pop.initialise()
    for i in range(10):
        print(pop.population[i])


if __name__ == '__main__':
    main()
