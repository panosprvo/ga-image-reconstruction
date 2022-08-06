from binary_image import *
from population_generation import *
from config import Config


class Fitness:
    def __init__(self):
        self.config = Config()
        self.fitness = self.config.GENOME_LENGTH * self.config.GENOME_LENGTH
        self.population_fitness = []

    def optimal_fitness_array(self):
        """
        This method is used to get the array of the image to be reconstructed. This is the array that will be used to
        compare each individual's array, therefore its fitness, while the algorithm is running.

        :return: a 2d binary array.
        """
        optimal_array = BinaryImage().open_original_image()
        return optimal_array

    def evaluate_fitness(self, optimal_array, individual_array):
        """
        This method is used to calculate the fitness level of an individual in the population, compared to the perfect
        individual, i.e., the array of the image to be reconstructed. It  stores the fitness of the individual in a
        list. This will be needed during selection and elitism.

        :param optimal_array: a 2d binary array.
        :param individual_array: a 2d binary array.

        :return: void
        """
        individual_fitness = self.fitness
        for i in range(self.config.GENOME_LENGTH):
            for j in range(self.config.GENOME_LENGTH):
                if optimal_array[i][j] == individual_array[i][j]:
                    continue
                else:
                    individual_fitness -= 1
        self.population_fitness.append(individual_fitness)


def main():
    population = InitialGeneration().initialise()
    fitness = Fitness()
    array1 = fitness.optimal_fitness_array()
    for i in range(10):
        fitness.evaluate_fitness(array1, population[i])
    print(fitness.population_fitness)
    print(f"Average fitness: {sum(fitness.population_fitness) / len(fitness.population_fitness)}")
    print(f"Max fitness: {max(fitness.population_fitness)}")
    print(f"Min fitness: {min(fitness.population_fitness)}")


if __name__ == '__main__':
    main()
