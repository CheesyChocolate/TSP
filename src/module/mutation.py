# This module contains functions for generating chromosome to the TSP problem.

# suppoted algorithms:
#   - random chromosome
#   - swap mutation


import random


from .data_calculator import trim
from .data_calculator import untrim


# generate random chromosome
# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @return: Type list
def generate_random_chromosome(tsp_data):
    # Extract city IDs from the dictionary keys
    chromosome = list(tsp_data.keys())
    # Remove gene 1 temporarily to ensure it's not in the middle of the chromosome
    chromosome.remove(1)
    random.shuffle(chromosome)
    # Ensure gene 1 appears both at the beginning and the end of the chromosome
    chromosome = untrim(chromosome)
    return chromosome


# swap mutation
# @param chromosome: Type list
# @return: Type list
def swap_mutation(chromosome):
    trimmed_chromosome = trim(chromosome)

    # Get two distinct random positions within the trimmed chromosome
    position1, position2 = random.sample(range(len(trimmed_chromosome)), 2)

    # Swap the genes at the selected positions in the trimmed chromosome
    trimmed_chromosome[position1], trimmed_chromosome[position2] = trimmed_chromosome[position2], trimmed_chromosome[position1]

    # Untrim the trimmed chromosome to restore the start and end genes (if necessary)
    untrimmed_chromosome = untrim(trimmed_chromosome)

    return untrimmed_chromosome
