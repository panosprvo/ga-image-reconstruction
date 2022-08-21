# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

import copy
import os
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

        # ======================= Algorithm loop ======================================================================
        crossover_operator_validation = ["S", "D", "U"]
        for crossover_operator in crossover_operator_validation:
            self.population = InitialGeneration().initialise()
            self.current_generation = []

            imaging = BinaryImage()
            fitness = Fitness()
            selection = Selection()
            crossover = Crossover()
            elitism = Elitism()

            # ======================= Optimal individual ==============================================================
            optimal_genotype = fitness.optimal_fitness_genotype()

            start_time = time.time()

            path = 'C:/Users/panos/Desktop/msc-computer-science-project/images'
            f = open(os.path.join(path, "algorithm_log.txt"), "a")

            maximum_algorithmic_fitness = 0
            max_fitness_in_generation = 0
            generation_list = []
            fitness_list = []

            for generation in range(self.config.GENERATIONS):
                generation_list.append(generation)
                print(f"Running generation: {generation + 1}")
                self.current_generation = self.population
                next_generation = []

                # ======================= Evaluate fitness for each individual ========================================
                for individual in self.current_generation:
                    fitness.evaluate_fitness(optimal_genotype, individual)

                # ======================= Seek elites in population ===================================================
                elites = elitism.find_elites(self.current_generation)
                for elite in elites:
                    next_generation.append(copy.deepcopy(elite))

                # ======================= Selection ===================================================================
                # The size of the population needs to stay the same throughout the run of the algorithm.
                # At this stage we already have the elites in the next generation.
                # Therefore, the size of the next population will be population - elites
                # Lastly, we divide this number by 2, as the following operations will be done in pairs of individual;
                # parent_one and parent_two, which will produce offspring_one and offspring_two

                for i in range(int((self.config.POPULATION - self.config.ELITE_CARRY_OVER) / 2)):
                    parent_one = selection.roulette_selection(self.current_generation)
                    parent_two = selection.roulette_selection(self.current_generation)

                    # ======================= Crossover ===============================================================
                    children = crossover.do_crossover(parent_one, parent_two, crossover_operator)

                    for child in children:
                        next_generation.append(copy.deepcopy(child))

                # ======================= Mutation ====================================================================
                for individual in next_generation:
                    individual.mutation()

                # ======================= Population fitness evaluation ===============================================
                # Update maximum fitness for the run of the algorithm.
                max_fitness_in_generation = fitness.get_max_fitness(next_generation)
                if fitness.get_max_fitness(next_generation) > maximum_algorithmic_fitness:
                    maximum_algorithmic_fitness = max_fitness_in_generation

                # Finish if algorithm has reached optimum fitness.
                if fitness.fitness_to_reach == max_fitness_in_generation:
                    print(f"Maximum fitness has been reached after {generation + 1} generations!")
                    top_individual = fitness.max_fitness_genotype(next_generation)
                    image = imaging.binary_array_to_binary_image(top_individual.genes)
                    helper.save_binary_image(image, generation, crossover_operator)
                    # Add this to the fitness_list otherwise trying to create the graph breaks cause x and y axes must
                    # have same first dimension
                    fitness_list.append(max_fitness_in_generation)
                    break
                else:
                    # Display maximum fitness for the generation and save an image every 100 generations.
                    print(f"Max fitness in current population is {max_fitness_in_generation}\n")
                    if generation % 100 == 0:
                        top_individual = fitness.max_fitness_genotype(next_generation)
                        image = imaging.binary_array_to_binary_image(top_individual.genes)
                        helper.save_binary_image(image, generation, crossover_operator)
                fitness_list.append(max_fitness_in_generation)

                # ======================= Prepare for next iteration ==================================================
                self.population = next_generation
                self.current_generation = []

            top_individual = fitness.max_fitness_genotype(next_generation)
            image = imaging.binary_array_to_binary_image(top_individual.genes)
            helper.save_binary_image(image, generation, crossover_operator)
            print(f"Maximum fitness for the run: {maximum_algorithmic_fitness}")
            helper.create_plot(generation_list, fitness_list, crossover_operator)

            # ======================= Update algorithm log ============================================================
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
