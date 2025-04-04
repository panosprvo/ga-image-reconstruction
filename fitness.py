# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

from binary_image import *
from config import Config


class Fitness(Config):
    def __init__(self):
        super().__init__()
        self.fitness_to_reach = self.GENOME_LENGTH * self.GENOME_LENGTH

    def optimal_fitness_genotype(self):
        """
        This method is used to get the array of the image to be reconstructed. This is the array that will be used to
        compare each individual's array, therefore its fitness, while the algorithm is running.

        :return: a Genotype object.
        """
        optimal_array = BinaryImage().open_original_image()
        return optimal_array

    def evaluate_fitness(self, optimal_genotype, individual_genotype):
        """
        This method is used to calculate the fitness level of an individual in the population, compared to the perfect
        individual, i.e., the array of the image to be reconstructed. It  stores the fitness of the individual in a
        list. This will be needed during selection and elitism.

        :param optimal_genotype: Genotype object.
        :param individual_genotype: Genotype object.

        :return: change an individual's fitness (void method).
        """
        individual_genotype.fitness = self.fitness_to_reach
        for i in range(self.GENOME_LENGTH):
            for j in range(self.GENOME_LENGTH):
                if optimal_genotype.genes[i][j] == individual_genotype.genes[i][j]:
                    continue
                else:
                    individual_genotype.fitness -= 1

    def get_max_fitness(self, population):
        """
        A method that returns the maximum fitness in a given population.

        :param population: an array of Genotype objects.

        :return: int.
        """
        return max(individual.fitness for individual in population)

    def max_fitness_genotype(self, population):
        """
        A method that returns the individual with the maximum fitness in a given population.

        :param population: an array of Genotype objects.

        :return: a Genotype object.
        """
        population.sort(key=lambda x: x.fitness, reverse=True)
        return population[0]
