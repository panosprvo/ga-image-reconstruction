import random

import numpy as np

from config import *


class CrossoverMethod:
    def __init__(self):
        self.config = Config()

    def generate_random_crossover_point(self):
        """
        Generate an integer number that will be used for the single point crossover method.

        :return: int
        """
        return random.randint(1, self.config.GENOME_LENGTH - 1)

    def single_point_crossover(self, genome_one, genome_two, crossover_point):
        """
        With this method, we select one crossover point.Each parental array is split into two parts. Combining a part
        of one parent with that one of the other parent, we generate two children.

        :param genome_one: numpy 2d array.
        :param genome_two: numpy 2d array.
        :param crossover_point: int.

        :return: an array consisting of two binary arrays (i.e., the two offspring).
        """
        child_one = np.append(genome_one[:crossover_point], genome_two[crossover_point:],
                              axis=0)
        child_two = np.append(genome_two[:crossover_point], genome_one[crossover_point:],
                              axis=0)
        offspring = [child_one, child_two]
        return offspring

    def double_point_crossover(self, genome_one, genome_two, crossover_point_one, crossover_point_two):
        """
        With this method, we randomly select two crossover points. We run a loop for those points using the single-point
        crossover method for each of the points.

        :param genome_one: numpy 2d array.
        :param genome_two: numpy 2d array.
        :param crossover_point_one: int.
        :param crossover_point_two: int.

        :return: an array consisting of two binary arrays (i.e., the two offspring).
        """
        points = np.array([crossover_point_one, crossover_point_two])

        # In case the random numbers generated are the same, rerun the method.
        while crossover_point_one == crossover_point_two:
            self.double_point_crossover(genome_one, genome_two, crossover_point_one, crossover_point_two)

        for index in points:
            genome_one, genome_two = self.single_point_crossover(genome_one, genome_two, index)
        offspring = [genome_one, genome_two]
        return offspring

    def uniform_crossover(self, genome_one, genome_two):
        """
        With this method, each bit is chosen in random from each parent using a probability matrix. In the end, we
        generate two children with genomes that can be widely different from the parental ones.

        :param genome_one: numpy 2d array.
        :param genome_two: numpy 2d array.

        :return: an array consisting of two binary arrays (i.e., the two offspring).
        """
        # Generate the probability matrix
        probability_matrix = np.random.rand(self.config.GENOME_LENGTH)
        for index in range(len(probability_matrix)):
            # Values less or greater than 0.5 can be considered here.
            if probability_matrix[index] < self.config.UNIFORM_PROBABILITY:
                temp = genome_one[index]
                genome_one[index] = genome_two[index]
                genome_two[index] = temp
        offspring = [genome_one, genome_two]
        return offspring


def main():
    return


if __name__ == '__main__':
    main()
