# This module contains functions for generating solutions to the TSP problem.
# suppoted algorithms:
#   - random solutions

import random


# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @return: Type list
def generate_random_solution(tsp_data):
    cities = list(tsp_data.keys())  # Extract city IDs from the dictionary keys
    cities.remove(1)  # Remove key 1 temporarily to ensure it's not in the middle of the solution
    random.shuffle(cities)
    # Ensure key 1 appears both at the beginning and the end of the solution
    solution = [1] + cities + [1]
    return solution
