import copy

import cv2

import helper
from binary_image import BinaryImage
from config import Config
from crossover import Crossover
from elitism import Elitism
from population_generation import InitialGeneration
from fitness import Fitness
from selection import Selection


class Algorithm:

    def __init__(self):
        self.config = Config()
        # ======================= Initialise the first generation =====================================================
        self.population = InitialGeneration().initialise()

    def run_algorithm(self):
        """

        :return:
        """
        imaging = BinaryImage()
        fitness = Fitness()
        selection = Selection()
        crossover = Crossover()
        elitism = Elitism()
        # ======================= Select crossover operator ===========================================================
        print("Please select the crossover method that will be used for this run of the algorithm.\n"
              "Press 1 for the single-point crossover operator, \n"
              "press 2 for the double-point crossover operator, \n"
              "or press 3 for the uniform crossover operator.")
        crossover_operator = int(input())
        crossover_operator_validation = [1, 2, 3]
        if crossover_operator not in crossover_operator_validation:
            print("You need to select an option from 1 to 3.")
            self.run_algorithm()
        # ======================= Optimal individual ==================================================================
        optimal_genotype = fitness.optimal_fitness_genotype()

        # ======================= Algorithm loop ======================================================================
        for generation in range(self.config.GENERATIONS):
            print(f"Running generation: {generation + 1}")
            current_generation = self.population
            next_generation = []

        # ======================= Evaluate fitness for each individual ================================================
            for individual in current_generation:
                fitness.evaluate_fitness(optimal_genotype, individual)

        # ======================= Seek elites in population ===========================================================
            elites = elitism.find_elites(current_generation)
            for elite in elites:
                next_generation.append(copy.deepcopy(elite))

        # ======================= Selection ===========================================================================
            # The size of the population needs to stay the same throughout the run of the algorithm.
            # At this stage we already have the elites in the next generation.
            # Therefore, the size of the next population will be population - elites
            # Lastly, we divide this number by 2, as the following operations will be done in pairs of individual;
            # parent_one and parent_two, which will produce offspring_one and offspring_two

            for i in range(int((self.config.POPULATION - self.config.ELITE_CARRY_OVER) / 2)):
                parent_one = selection.roulette_selection(current_generation)
                parent_two = selection.roulette_selection(current_generation)

        # ======================= Crossover ===========================================================================
                if crossover_operator == 1:
                    crossover_point = crossover.generate_random_crossover_point()
                    children = crossover.single_point_crossover(parent_one, parent_two, crossover_point)
                elif crossover_operator == 2:
                    crossover_point_one = crossover.generate_random_crossover_point()
                    crossover_point_two = crossover.generate_random_crossover_point()
                    children = crossover.double_point_crossover(parent_one, parent_two,
                                                                crossover_point_one, crossover_point_two)
                else:
                    children = crossover.uniform_crossover(parent_one, parent_two)

                for child in children:
                    next_generation.append(copy.deepcopy(child))

        # ======================= Mutation ============================================================================
            for individual in next_generation:
                individual.mutation()

        # ======================= Population fitness evaluation =======================================================
            if fitness.fitness_to_reach == fitness.get_max_fitness(next_generation):
                print(f"Maximum fitness has been reached after {generation + 1} generations!")
                top_individual = fitness.max_fitness_genotype(next_generation)
                image = imaging.binary_array_to_binary_image(top_individual.genes)
                helper.save_binary_image(image, generation)
                break
            else:
                print(f"Max fitness in current population(generation {generation + 1}) is "
                      f"{fitness.get_max_fitness(next_generation)}")
                if generation % 20 == 0:
                    top_individual = fitness.max_fitness_genotype(next_generation)
                    image = imaging.binary_array_to_binary_image(top_individual.genes)
                    helper.save_binary_image(image, generation)
        # ======================= Prepare for next iteration ==========================================================
            self.population = next_generation
            print("Press any button when you are ready to run the next iteration of the algorithm.\n")
            # input("Press Enter to continue...")


def main():
    algorithm = Algorithm()
    algorithm.run_algorithm()


if __name__ == '__main__':
    main()
