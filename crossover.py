import random

import numpy as np

from binary_image import BinaryImage
from config import *
from genotype import Genotype


class CrossoverMethod:
    def __init__(self):
        self.config = Config()

    def generate_random_crossover_point(self):
        """
        Generate an integer number that will be used for the single point crossover method.

        :return: int
        """
        return random.randint(1, self.config.GENOME_LENGTH - 1)

    def single_point_crossover(self, genotype_one, genotype_two, crossover_point):
        """
        With this method, we select one crossover point. Each parental array is split into two parts. Combining a part
        of one parent with that one of the other parent, we generate two children.

        :param genotype_one: Genotype object.
        :param genotype_two: Genotype object.
        :param crossover_point: int.

        :return: an array consisting of two Genotype objects (i.e., the two offspring).
        """
        child_one_genotype = genotype_one.genes[:crossover_point] + genotype_two.genes[crossover_point:]
        child_two_genotype = genotype_two.genes[:crossover_point] + genotype_one.genes[crossover_point:]
        child_one = Genotype()
        child_one.genes = child_one_genotype
        child_two = Genotype()
        child_two.genes = child_two_genotype
        return [child_one, child_two]

    def double_point_crossover(self, genotype_one, genotype_two, crossover_point_one, crossover_point_two):
        """
        With this method, we randomly select two crossover points. We run a loop for those points using the single-point
        crossover method for each of the points.

        :param genotype_one: Genotype object.
        :param genotype_two: Genotype object.
        :param crossover_point_one: int.
        :param crossover_point_two: int.

        :return: an array consisting of two Genotype objects (i.e., the two offspring).
        """
        points = [crossover_point_one, crossover_point_two]

        # In case the random numbers generated are the same, rerun.
        while crossover_point_one == crossover_point_two:
            self.double_point_crossover(genotype_one, genotype_two, crossover_point_one, crossover_point_two)

        for index in points:
            genotype_one, genotype_two = self.single_point_crossover(genotype_one, genotype_two, index)
        return [genotype_one, genotype_two]

    def uniform_crossover(self, genotype_one, genotype_two):
        """
        With this method, each bit is chosen in random from each parent using a probability matrix. In the end, we
        generate two children with genomes that can be widely different from the parental ones.

        :param genotype_one: Genotype object.
        :param genotype_two: Genotype object.

        :return: an array consisting of two Genotype objects (i.e., the two offspring).
        """
        # Generate the probability matrix
        probability_matrix = np.random.rand(self.config.GENOME_LENGTH)
        for index in range(len(probability_matrix)):
            # Values less or greater than 0.5 can be considered here.
            if probability_matrix[index] < self.config.UNIFORM_PROBABILITY:
                temp = genotype_one.genes[index]
                genotype_one.genes[index] = genotype_two.genes[index]
                genotype_two.genes[index] = temp
        return [genotype_one, genotype_two]


def main():
    par1 = Genotype()
    par2 = Genotype()
    print(f"Parent1: {par1.genes}")
    print(f"Parent2: {par2.genes}")

    cross = CrossoverMethod()
    kids = cross.uniform_crossover(par1, par2)
    print(f"Child1: {kids[0].genes}")
    print(f"Child2: {kids[1].genes}")
    print(type(kids[0]))


if __name__ == '__main__':
    main()
