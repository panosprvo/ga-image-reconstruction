from config import Config


class Elitism:

    def __init__(self):
        self.config = Config()

    def find_elites(self, pop_fitness, population):
        """
        This method sorts the fitness of all individuals in order to get the indices of the individuals with the highest
        fitness. Then we grab those individuals and store them in a new list. In case there are individuals with the
        same fitness on the cut-off point, we select the individual with the higher index.

        :param pop_fitness: list that holds the fitness of all individuals in the current generation.
        :param population: list that holds the genetic information of all individuals in the current generation.

        :return: array of individuals to be included in the next generation without any crossover/mutation applied.
        """
        elites = []
        elites_indices = sorted(range(len(pop_fitness)), key=lambda i: pop_fitness[i])[-self.config.ELITE_CARRY_OVER:]

        for index in elites_indices:
            elites.append(population[index])
        return elites


def main():
    return


if __name__ == '__main__':
    main()
