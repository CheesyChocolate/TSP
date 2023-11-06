# This module contains functions for generating solutions to the TSP problem.
# suppoted algorithms:
#   - random solutions


import random


# @param node_coords: Type dict (NODE_COORD_SECTION)
# @return: Type list
def generate_random_solution(node_coords):
    city_ids = list(node_coords.keys())  # Extract city IDs from the dictionary
    random.shuffle(city_ids)  # Shuffle the city IDs randomly
    return city_ids
