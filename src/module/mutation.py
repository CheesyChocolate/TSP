# This module contains functions for generating chromosome to the TSP problem.

# suppoted algorithms:
#   - random chromosome


import random


# generate random chromosome
# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @return: Type list
def generate_random_chromosome(tsp_data):
    cities = list(tsp_data.keys())  # Extract city IDs from the dictionary keys
    cities.remove(1)  # Remove key 1 temporarily to ensure it's not in the middle of the chromosome
    random.shuffle(cities)
    # Ensure key 1 appears both at the beginning and the end of the chromosome
    chromosome = [1] + cities + [1]
    return chromosome
