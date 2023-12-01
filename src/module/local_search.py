# Description: This file contains the implementation of local search algorithm
# used to improve the solution of the genetic algorithm.

# supported algorithms:
# - 2-opt

from .data_calculator import fitness
from .mutation import inversion_mutation


# 2-opt local search algorithm
# @param chromosome: Type list
# @param node_cords: type dict (NODE_CORD_SECTION)
# @return: Type list
def two_opt(chromosome, node_cords):
    num_cities = len(chromosome)
    best_distance = fitness(chromosome, node_cords)

    improved = True
    while improved:
        improved = False
        for i in range(1, num_cities - 1):
            for k in range(i + 1, num_cities):
                # Apply inversion mutation to generate a new candidate solution
                new_chromosome = inversion_mutation(chromosome, i, k)

                # Calculate the fitness of the new solution
                new_distance = fitness(new_chromosome, node_cords)

                # If the new solution is better, update the chromosome and distance
                if new_distance < best_distance:
                    chromosome = new_chromosome
                    best_distance = new_distance
                    improved = True
                    break
            if improved:
                break

    return chromosome
