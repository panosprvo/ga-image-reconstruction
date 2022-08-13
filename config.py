# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

class Config:
    def __init__(self):
        self.GENERATIONS = 1000
        self.POPULATION = 300
        self.GENOME_LENGTH = 32
        self.MUTATION_PROBABILITY = 0.002
        self.ELITE_CARRY_OVER = int(self.POPULATION * 0.04)
        self.WHITE_RATIO = 0.5
        self.UNIFORM_PROBABILITY = 0.5
