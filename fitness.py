from binary_image import *
from genotype import Genotype
from population_generation import *
from config import Config


class Fitness:
    def __init__(self):
        self.config = Config()
        self.fitness = self.config.GENOME_LENGTH * self.config.GENOME_LENGTH

    def optimal_fitness_array(self):
        """
        This method is used to get the array of the image to be reconstructed. This is the array that will be used to
        compare each individual's array, therefore its fitness, while the algorithm is running.

        :return: a 2d binary array.
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
        individual_genotype.fitness = self.fitness
        for i in range(self.config.GENOME_LENGTH):
            for j in range(self.config.GENOME_LENGTH):
                if optimal_genotype.genes[i][j] == individual_genotype.genes[i][j]:
                    continue
                else:
                    individual_genotype.fitness -= 1


def main():
    population = InitialGeneration().initialise()
    fitness = Fitness()
    genes = fitness.optimal_fitness_array()
    optimal_array = Genotype()
    optimal_array.genes = genes

    for i in range(10):
        fitness.evaluate_fitness(optimal_array, population[i])
        print(population[i].fitness)
    print(f"Average fitness: {sum(i.fitness for i in population) / 10}")
    print(f"Max fitness: {max(i.fitness for i in population)}")
    print(f"Min fitness: {min(i.fitness for i in population)}")


if __name__ == '__main__':
    main()
