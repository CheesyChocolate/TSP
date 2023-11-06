# This module contains functions for generating solutions to the TSP problem.
# suppoted algorithms:
#   - random solutions

import random


def generate_random_solutions(tsp_data, num_solutions):
    cities = tsp_data['NODE_COORD_SECTION']
    random_solutions = []

    for _ in range(num_solutions):
        # Generate a random permutation of city indices excluding the first city (starting point)
        solution = [city[0] for city in cities[1:]]
        random.shuffle(solution)
        # Add the starting city back to the beginning of the solution
        solution.insert(0, cities[0][0])
        random_solutions.append(solution)

    return random_solutions
