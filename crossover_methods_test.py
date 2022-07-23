import numpy

import config
from crossover_methods import *


def test_single_point_crossover():
    config.genome_length = 4
    genome_one = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0]]
    genome_two = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 0]]
    print(single_point_crossover(genome_one, genome_two))
