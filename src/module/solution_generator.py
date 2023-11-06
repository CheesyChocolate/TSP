# This module contains functions for generating solutions to the TSP problem.
# suppoted algorithms:
#   - random solutions

import random


# @param tsp_data: Type dict
# @return: Type 2D list
def generate_random_solution(tsp_data):
    cities = tsp_data['NODE_COORD_SECTION']
    # Generate a random permutation of city indices excluding the first city (starting point)
    solution = [city[0] for city in cities[1:]]
    random.shuffle(solution)
    # Add the starting city back to the beginning of the solution
    solution.insert(0, cities[0][0])

    return [solution]
