# This module contains functions for calculation related to
# the data in the TSP problem
# Implemented functions:
#   calculate_distance(point1, point2)
#   calculate_total_distance(solution, node_coords)

import math


# Calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Calculate total distance traveled for the given solution
# @param solution: Type list
# @param node_coords: Type dict (NODE_COORD_SECTION)
# @return: Type float
def calculate_total_distance(solution, node_coords):
    total_distance = 0.0

    # Calculate total distance by summing distances between consecutive cities in the solution
    for i in range(len(solution) - 1):
        total_distance += calculate_distance(node_coords[solution[i]], node_coords[solution[i+1]])

    return total_distance
