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
def generate_random_chromosome(tsp_data, close_loop=True):
    # Extract city IDs from the dictionary keys
    chromosome = list(tsp_data.keys())
    # if a close loop is required, add the first city to the end of the chromosome
    if close_loop:
        chromosome.append(chromosome[0])
    # trim the chromosome (the trim function handles either the loop is closed or not)
    trimmed_chromosome, trimmed_gene = trim(chromosome)
    # shuffle the chromosome
    random.shuffle(trimmed_chromosome)
    # untrim the chromosome
    untrimmed_chromosome = untrim(trimmed_chromosome, trimmed_gene)
    return untrimmed_chromosome


# swap mutation
# @param chromosome: Type list
# @return: Type list
def swap_mutation(chromosome):
    trimmed_chromosome, trimmed_gene = trim(chromosome)

    # Get two distinct random positions within the trimmed chromosome
    position1, position2 = random.sample(range(len(trimmed_chromosome)), 2)

    # Swap the genes at the selected positions in the trimmed chromosome
    trimmed_chromosome[position1], trimmed_chromosome[position2] = trimmed_chromosome[position2], trimmed_chromosome[position1]

    # Untrim the trimmed chromosome to restore the start and end genes (if necessary)
    untrimmed_chromosome = untrim(trimmed_chromosome, trimmed_gene)

    return untrimmed_chromosome
