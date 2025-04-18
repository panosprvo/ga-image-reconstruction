# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

from config import Config


class Elitism(Config):

    def __init__(self):
        super().__init__()

    def find_elites(self, population):
        """
        This method sorts the fitness of all individuals in order to get the indices of the individuals with the highest
        fitness. Then we grab those individuals and store them in a new list. In case there are individuals with the
        same fitness on the cut-off point, we select the individual with the higher index.

        :param population: list that holds the genetic information of all individuals in the current generation.

        :return: array of individuals to be included in the next generation without any crossover/mutation applied.
        """
        elites = []
        fitness = []
        for individual in population:
            fitness.append(individual.fitness)
        elites_indices = sorted(range(len(fitness)),
                                key=lambda i: fitness[i])[-self.ELITE_CARRY_OVER:]

        for index in elites_indices:
            elites.append(population[index])
        return elites
