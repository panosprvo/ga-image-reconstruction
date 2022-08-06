import numpy.random as npr

from config import Config
from population_generation import InitialGeneration


class Selection:

    def __init__(self):
        self.config = Config()

    def roulette_selection(self, population):
        """
        For the selection operator we are using the roulette-wheel operator (read README for more information). This
        method is selecting an individual from the population that will be used to create offspring for the next
        generation.

        :return: Genotype object.
        """
        cumulative_fitness = sum(individual.fitness for individual in population)
        selection_probability = [individual.fitness/cumulative_fitness for individual in population]
        return population[npr.choice(len(population), p=selection_probability)]


def main():
    selection = Selection()
    init_population = InitialGeneration()
    population = init_population.initialise()
    population[0].fitness = 502
    population[1].fitness = 516
    population[2].fitness = 530
    population[3].fitness = 523
    population[4].fitness = 520
    population[5].fitness = 516
    population[6].fitness = 493
    population[7].fitness = 506
    population[8].fitness = 512
    population[9].fitness = 509
    for i in range(50):
        print((selection.roulette_selection(population)).genes)


if __name__ == '__main__':
    main()
