from binary_image import *
from genotype import Genotype
from population_generation import *
from config import Config


class Fitness:
    def __init__(self):
        self.config = Config()
        self.fitness_to_reach = self.config.GENOME_LENGTH * self.config.GENOME_LENGTH

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
        for i in range(self.config.GENOME_LENGTH):
            for j in range(self.config.GENOME_LENGTH):
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


def main():
    population = InitialGeneration().initialise()
    fitness = Fitness()
    genes = fitness.optimal_fitness_genotype()
    optimal_array = Genotype()
    optimal_array.genes = genes

    for i in range(10):
        fitness.evaluate_fitness(optimal_array, population[i])
        print(population[i].fitness_to_reach)
    print(f"Average fitness: {sum(i.fitness_to_reach for i in population) / 10}")
    print(f"Max fitness: {max(i.fitness_to_reach for i in population)}")
    print(f"Min fitness: {min(i.fitness_to_reach for i in population)}")


if __name__ == '__main__':
    main()
