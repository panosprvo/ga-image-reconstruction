# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

import copy
import time

import helper
from binary_image import BinaryImage
from config import Config
from crossover import Crossover
from elitism import Elitism
from initial_generation import InitialGeneration
from fitness import Fitness
from selection import Selection


class Algorithm:

    def __init__(self):
        self.config = Config()
        # ======================= Initialise the first generation =====================================================
        self.population = InitialGeneration().initialise()
        self.current_generation = []

    def run_algorithm(self):
        """
        The method that runs the algorithm.

        :return: prints results in terminal, and saves images and graphs for each run.
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
        maximum_algorithmic_fitness = 0
        max_fitness_in_generation = 0

        start_time = time.time()
        f = open("algorithm_log.txt", "a")

        generation_list = []
        fitness_list = []
        for generation in range(self.config.GENERATIONS):
            generation_list.append(generation)
            print(f"Running generation: {generation + 1}")
            self.current_generation = self.population
            next_generation = []

        # ======================= Evaluate fitness for each individual ================================================
            for individual in self.current_generation:
                fitness.evaluate_fitness(optimal_genotype, individual)

        # ======================= Seek elites in population ===========================================================
            elites = elitism.find_elites(self.current_generation)
            for elite in elites:
                next_generation.append(copy.deepcopy(elite))

        # ======================= Selection ===========================================================================
            # The size of the population needs to stay the same throughout the run of the algorithm.
            # At this stage we already have the elites in the next generation.
            # Therefore, the size of the next population will be population - elites
            # Lastly, we divide this number by 2, as the following operations will be done in pairs of individual;
            # parent_one and parent_two, which will produce offspring_one and offspring_two

            for i in range(int((self.config.POPULATION - self.config.ELITE_CARRY_OVER) / 2)):
                parent_one = selection.roulette_selection(self.current_generation)
                parent_two = selection.roulette_selection(self.current_generation)

        # ======================= Crossover ===========================================================================
                children = crossover.do_crossover(parent_one, parent_two, crossover_operator)

                for child in children:
                    next_generation.append(copy.deepcopy(child))

        # ======================= Mutation ============================================================================
            for individual in next_generation:
                individual.mutation()

        # ======================= Population fitness evaluation =======================================================
            # Update maximum fitness for the run of the algorithm.
            max_fitness_in_generation = fitness.get_max_fitness(next_generation)
            if fitness.get_max_fitness(next_generation) > maximum_algorithmic_fitness:
                maximum_algorithmic_fitness = max_fitness_in_generation

            # Finish if algorithm has reached optimum fitness.
            if fitness.fitness_to_reach == max_fitness_in_generation:
                print(f"Maximum fitness has been reached after {generation + 1} generations!")
                top_individual = fitness.max_fitness_genotype(next_generation)
                image = imaging.binary_array_to_binary_image(top_individual.genes)
                helper.save_binary_image(image, generation)
                break
            else:
                # Display maximum fitness for the generation and save an image every 50 generations.
                print(f"Max fitness in current population(generation {generation + 1}) is "
                      f"{max_fitness_in_generation}\n")
                if generation % 50 == 0:
                    top_individual = fitness.max_fitness_genotype(next_generation)
                    image = imaging.binary_array_to_binary_image(top_individual.genes)
                    helper.save_binary_image(image, generation)
            fitness_list.append(max_fitness_in_generation)

        # ======================= Prepare for next iteration ==========================================================
            self.population = next_generation
            self.current_generation = []

        print(f"Maximum fitness for the run: {maximum_algorithmic_fitness}")
        helper.create_plot(generation_list, fitness_list)

        # ======================= Update algorithm log ================================================================
        end_time = time.time()
        total_runtime = "%.2f" % (end_time - start_time)
        time_of_run = time.strftime("%d%m%Y-%H%M%S")
        reach_global_optimum = "No"
        if fitness.fitness_to_reach == max_fitness_in_generation:
            reach_global_optimum = 'Yes'
        f.write(f"{time_of_run}\n")
        f.write(f"Did the algorithm reach maximum fitness? : {reach_global_optimum}\n")
        f.write(f"Crossover method used: {str(crossover_operator)}\n")
        f.write(f"Population size: {self.config.POPULATION}\n")
        f.write(f"Number of generations: {self.config.GENERATIONS}\n")
        f.write(f"Mutation probability: {self.config.MUTATION_PROBABILITY}\n")
        f.write(f"Number of elites in each generation: {self.config.ELITE_CARRY_OVER}\n")
        f.write(f"Maximum fitness reached: {maximum_algorithmic_fitness}/{fitness.fitness_to_reach}\n")
        f.write(f"Total runtime: {total_runtime} seconds\n")
        f.write("\n")
        f.close()


def main():
    Algorithm().run_algorithm()


if __name__ == '__main__':
    main()
