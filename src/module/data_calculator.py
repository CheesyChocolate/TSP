# This module contains functions for calculation related to
# the data in the TSP problem
# Implemented functions:
#   calculate_distance_matrix(node_coords)
#   calculate_total_distance(chromosome, dist_matrix)
#   calculate_fitness(chromosome, node_coords)
#   trim(chromosome)
#   untrim(chromosome, trimed_gene=1)

# importing sqrt function from numpy module for better performance
from scipy.spatial import distance_matrix


# Calculate the distance between two points
# This function should be separated from 'calculate_distance_matrix'
# since we need this calculation once per run (not once per generation)
# @param point1: Type Dict (NODE_COORD_SECTION)
# @return: Type matrix
def calculate_distance_matrix(node_coords):
    # Convert node coordinates to a list
    coords_list = list(node_coords.values())
    # Compute the distance matrix using scipy's distance_matrix function
    dist_matrix = distance_matrix(coords_list, coords_list)

    return dist_matrix


# Calculate the distance of the given chromosome
# @param chromosome: Type list
# @param dist_matrix: Type Matrix
# @return: Type float
def calculate_total_distance(chromosome, dist_matrix):
    total_distance = 0.0
    for i in range(len(chromosome) - 1):
        # TODO: -1 is used to map the node ID to the index of the distance in the matrix
        #  This is not a good practice, find a better way to do this
        #  What is the node ID is not in order? or ID is not number? or ID starts from 0?
        #  a dictionary?
        total_distance += dist_matrix[chromosome[i] - 1][chromosome[i + 1] - 1]
    return total_distance


# Calculate fitness for a given chromosome
# @param chromosome: Type list
# @param dist_matrix: Type Matrix
# @return: Type float
def fitness(chromosome, dist_matrix):
    return 1 / calculate_total_distance(chromosome, dist_matrix)


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
