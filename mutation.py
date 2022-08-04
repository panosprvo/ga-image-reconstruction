import copy
import random

import numpy as np

from binary_image import BinaryImage
from config import Config


class Mutation:

    def __init__(self, individual):
        self.config = Config()
        self.genome = individual

    def do_mutation(self):
        """
        Depending on config.MUTATION_PROBABILITY, we produce a random number between 0 and 1 to decide whether a
        mutation for the specific gene should take place or not. Mutation is the reversal of 0 to 1, and 1 to 0.
        :return: void - method that only flips genes that should be mutated.
        """
        for j in range(self.config.GENOME_LENGTH):
            for index in range(self.config.GENOME_LENGTH):
                if random.uniform(0, 1) <= self.config.MUTATION_PROBABILITY:
                    self.genome[j][index] = self.__mutate(self.genome[j][index])
        # print(f"M: {self.genome}")

    def __mutate(self, gene):
        if gene == 0:
            return 1
        return 0


def main():
    bi1 = BinaryImage()
    img1 = bi1.create_random_binary_image()
    par1 = bi1.binary_image_to_binary_array(img1)

    mut = Mutation(par1)
    original = copy.deepcopy(mut.genome)
    print(f"I: {mut.genome}")
    mut.do_mutation()
    print(f"M: {mut.genome}")
    print(np.array_equal(mut.genome, original))


if __name__ == '__main__':
    main()
