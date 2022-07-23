import random

from config import Config


class Chromosome:

    def __init__(self):
        self.config = Config()
        self.genome = [random.randint(0, 1) for _ in range(self.config.GENOME_LENGTH)]

    def do_mutation(self):
        """
        Depending on config.MUTATION_PROBABILITY, we
        :return:
        """
        for index in range(self.config.GENOME_LENGTH):
            if random.uniform(0, 1) <= self.config.MUTATION_PROBABILITY:
                self.genome[index] = self.mutate(self.genome[index])

    def mutate(self, gene):
        if gene == 0:
            return 1
        return 0


def main():
    return


if __name__ == '__main__':
    main()
