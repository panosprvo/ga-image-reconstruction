# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

import random

import numpy as np

from config import *


class Crossover:
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
        genotype_one.genes, genotype_two.genes = genotype_one.genes[:crossover_point] + genotype_two.genes[crossover_point:], \
                                     genotype_two.genes[:crossover_point] + genotype_one.genes[crossover_point:]
        return [genotype_one, genotype_two]

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
            crossover_point_one = self.generate_random_crossover_point()
            crossover_point_two = self.generate_random_crossover_point()
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
                genotype_one.genes[index], genotype_two.genes[index] = \
                    genotype_two.genes[index], genotype_one.genes[index]
        return [genotype_one, genotype_two]

    def do_crossover(self, parent_one, parent_two, crossover_operator):
        """
        Method that returns the children after crossover of two parents selected for reproduction.

        :param parent_two: a Genotype object.
        :param parent_one: a Genotype object.
        :param crossover_operator: int.

        :return: a list of two Genotype objects.
        """
        if crossover_operator == 1:
            crossover_point = self.generate_random_crossover_point()
            children = self.single_point_crossover(parent_one, parent_two, crossover_point)
        elif crossover_operator == 2:
            crossover_point_one = self.generate_random_crossover_point()
            crossover_point_two = self.generate_random_crossover_point()
            children = self.double_point_crossover(parent_one, parent_two,
                                                        crossover_point_one, crossover_point_two)
        else:
            children = self.uniform_crossover(parent_one, parent_two)
        return children
