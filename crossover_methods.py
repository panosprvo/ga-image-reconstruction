import random

import numpy as np

from config import *


class CrossoverMethod:
    def __init__(self, genome_one, genome_two):
        self.config = Config()
        self.genome_one = genome_one
        self.genome_two = genome_two

    def single_point_crossover(self, genome_one, genome_two):
        """
        With this method, we randomly select one crossover point.Each parental array is split into two parts.
        Combining a part of one parent with that one of the other parent, we generate two children.
        :param genome_one: binary array from the first parent.
        :param genome_two: binary array from the second parent.
        :return: an array consisting of two binary arrays (i.e., the two offspring).
        """
        crossover_point = random.randint(1, self.config.GENOME_LENGTH - 1)
        child_one = np.append(genome_one[:crossover_point], genome_two[crossover_point:])
        child_two = np.append(genome_two[:crossover_point], genome_one[crossover_point:])
        offspring = [child_one, child_two]
        return offspring

    def double_point_crossover(self, genome_one, genome_two):
        """
        With this method, we randomly select two crossover points. Each parental array is split into three parts.
        These are used to generate two children.
        :param genome_one: binary array from the first parent.
        :param genome_two: binary array from the second parent.
        :return: an array consisting of two binary arrays (i.e., the two offspring).
        """
        crossover_point_one = random.randint(1, self.config.GENOME_LENGTH - 1)
        crossover_point_two = random.randint(1, self.config.GENOME_LENGTH - 1)
        while crossover_point_one == crossover_point_two:
            self.double_point_crossover(genome_one, genome_two)
            print("Retrying...")

        crossover_point_lesser = crossover_point_greater = 0
        if crossover_point_one < crossover_point_two:
            crossover_point_lesser = crossover_point_one
            crossover_point_greater = crossover_point_two

        child_one = np.append(genome_one[:crossover_point_lesser],
                              genome_two[crossover_point_lesser:crossover_point_greater],
                              genome_one[crossover_point_greater:])

        child_two = np.append(genome_two[:crossover_point_lesser],
                              genome_one[crossover_point_lesser:crossover_point_greater],
                              genome_two[crossover_point_greater:])

        offspring = [child_one, child_two]
        return offspring

    def uniform_crossover(self, genome_one, genome_two):
        """
        With this method, each bit is chosen in random from each parent. In the end, we generate two children with
        genomes that can be extremely different from the parental ones.
        :param genome_one: binary array from the first parent.
        :param genome_two: binary array from the second parent.
        :return: an array consisting of two binary arrays (i.e., the two offspring).
        """
        child_one = []
        child_two = []
        for i in range(len(self.config.GENOME_LENGTH)):
            parent_selector = random.randint(0, 1)
            if parent_selector == 0:
                child_one[i] = genome_one[i]
                child_two[i] = genome_two[i]
            elif parent_selector == 1:
                child_one[i] = genome_two[i]
                child_two[i] = genome_one[i]
        offspring = [child_one, child_two]
        return offspring


def main():
    genome_one = np.a


if __name__ == '__main__':
    main()
