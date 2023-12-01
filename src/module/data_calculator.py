# This module contains functions for calculation related to
# the data in the TSP problem
# Implemented functions:
#   calculate_distance(point1, point2)
#   fitness(chromosome, node_coords)
#   trim(chromosome)
#   untrim(chromosome, trimed_gene=1)

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


# Trim the chromosome by removing the first and last gene if they are the same
# @param chromosome: Type list
# @return: Type list
# @return: Type int(or ID of the trimmed gene) can be None
def trim(chromosome):
    trimmed_gene = None
    if chromosome[0] == chromosome[-1]:
        trimmed_gene = chromosome[0]
        return chromosome[1:-1], trimmed_gene
    return chromosome, trimmed_gene


# Add the starting gene to the beginning and end of the chromosome
# @param chromosome: Type list
# @param trimed_gene: Type int
# @return: Type list
def untrim(chromosome, trimmed_gene=None):
    if trimmed_gene is not None:
        return [trimmed_gene] + chromosome + [trimmed_gene]
    return chromosome
