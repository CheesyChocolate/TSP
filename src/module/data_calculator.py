# This module contains functions for calculation related to
# the data in the TSP problem
# Implemented functions:
#   calculate_distance(point1, point2)
#   fitness(chromosome, node_coords)

import math


# Calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Calculate total distance traveled for the given chromosome
# @param chromosome: Type list
# @param node_coords: Type dict (NODE_COORD_SECTION)
# @return: Type float
def fitness(chromosome, node_coords):
    total_distance = 0.0

    # Calculate total distance by summing distances between consecutive cities in the chromosome
    for i in range(len(chromosome) - 1):
        total_distance += calculate_distance(node_coords[chromosome[i]], node_coords[chromosome[i+1]])

    return total_distance
