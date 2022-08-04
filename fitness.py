from binary_image import *
from population_generation import *
from config import Config


class Fitness:
    def __init__(self):
        self.config = Config()
        self.fitness = self.config.GENOME_LENGTH * self.config.GENOME_LENGTH

    def optimal_fitness_array(self, img):
        """
        This method is used to get the array of the image to be reconstructed. This is the array that will be used to
        compare each individual's array, therefore its fitness, while the algorithm is running.

        :param img: a png file of the image to be reconstructed.

        :return: a 2d binary array.
        """
        optimal_array = BinaryImage().open_original_image(img)
        return optimal_array

    def evaluate_fitness(self, optimal_array, individual_array):
        """
        This method is used to calculate the fitness level of an individual in the population, compared to the perfect
        individual, i.e., the array of the image to be reconstructed.

        :param optimal_array: a 2d binary array.
        :param individual_array: a 2d binary array.

        :return: int; the fitness level of the individual, whose genome is being compared to the optimal_array.
        """
        individual_fitness = self.fitness
        for i in range(self.config.GENOME_LENGTH):
            for j in range(self.config.GENOME_LENGTH):
                if optimal_array[i][j] == individual_array[i][j]:
                    continue
                else:
                    individual_fitness -= 1
        return individual_fitness


def main():
    population = InitialGeneration().initialise()
    fitness = Fitness()
    original_image = BinaryImage().open_original_image("original_image.png")
    array1 = fitness.optimal_fitness_array(original_image)
    individual_fitness = [None] * 200
    for i in range(200):
        individual_fitness[i] = fitness.evaluate_fitness(array1, population[i])
    print(f"Max fitness: {max(individual_fitness)}")
    print(f"Min fitness: {min(individual_fitness)}")


if __name__ == '__main__':
    main()
