# Description: This file contains the implementation of local search algorithm
# used to improve the solution of the genetic algorithm.

# supported algorithms:
# - 2-opt
# - 2-opt with a stopping criterion (partial 2-opt)

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


# 2-opt local search algorithm with a stopping criterion and a maximum number of iterations
# FUN COMMENT: Brain me BIG!!!!
# TODO: fiteness threshold can be dynamic. more iterations -> lower threshold
# @param chromosome: Type list
# @param tsp_data: type dict (TSP_DATA_SECTION)
# @param max_iterations: type int
# @param fitness_threshold: type float
# @return: Type list
def partial_two_opt(chromosome, tsp_data, max_iterations=20, fitness_threshold=0.001):
    # Initial fitness calculation
    current_fitness = fitness(chromosome, tsp_data)
    n = len(chromosome)  # Number of genes in the chromosome

    # Perform the 2-opt local search for a certain number of iterations
    for iteration in range(max_iterations):
        best_improvement = 0.0
        best_i, best_k = None, None

        # Iterate over the chromosome to find the best improvement
        # TODO: start form different positions in the chromosome for each iteration
        for i in range(1, n - 1):
            for k in range(i + 2, n - 1):
                # Apply inversion mutation to create a new chromosome
                new_chromosome = inversion_mutation(chromosome, i, k)
                new_fitness = fitness(new_chromosome, tsp_data)

                # Calculate the improvement in fitness
                improvement = current_fitness - new_fitness

                # Check if the new solution is better
                if improvement > best_improvement:
                    best_improvement = improvement
                    best_i, best_k = i, k

                # Check if the improvement meets the fitness threshold
                if best_improvement >= fitness_threshold:
                    break  # Exit the inner loop

            # Check if the improvement meets the fitness threshold
            if best_improvement >= fitness_threshold:
                break  # Exit the outer loop

        # If no significant improvements found, terminate the search
        if best_improvement < fitness_threshold:
            break

        # Apply the best inversion mutation found
        chromosome = inversion_mutation(chromosome, best_i, best_k)
        current_fitness -= best_improvement  # Update current fitness

    return chromosome


# 3-opt local search algorithm
# @param chromosome: Type list
# @param node_cords: type dict (NODE_CORD_SECTION)
# @return: Type list
def three_opt(chromosome, node_cords):
    num_cities = len(chromosome)
    best_distance = fitness(chromosome, node_cords)

    improved = True
    while improved:
        improved = False
        for i in range(1, num_cities - 2):
            for j in range(i + 1, num_cities - 1):
                for k in range(j + 1, num_cities):
                    # Apply 3-opt moves to generate new candidate solutions
                    new_chromosome = three_opt_move(chromosome, node_cords, i, j, k)

                    # Calculate the fitness of the new solution
                    new_distance = fitness(new_chromosome, node_cords)

                    # If the new solution is better, update the chromosome and distance
                    if new_distance < best_distance:
                        chromosome = new_chromosome
                        best_distance = new_distance
                        improved = True  # Set flag to continue outer loop
                        break  # Innermost loop breaks to generate new solutions
                if improved:
                    break  # Middle loop breaks if improvement occurred
            if improved:
                break  # Outer loop breaks if improvement occurred
    return chromosome


def three_opt_move(chromosome, node_cords, i, j, k):
    # Extract segments of the chromosome based on indices i, j, and k
    segment1 = chromosome[:i]
    segment2 = chromosome[i:j]
    segment3 = chromosome[j:k]
    segment4 = chromosome[k:]

    # Combine the segments in different orderings to create new candidate solutions
    new_chromosome1 = segment1 + segment3 + segment2 + segment4
    new_chromosome2 = segment1 + segment4 + segment3 + segment2
    new_chromosome3 = segment1 + segment2 + segment4 + segment3

    # Calculate the fitness of the new solutions
    fitness1 = fitness(new_chromosome1, node_cords)
    fitness2 = fitness(new_chromosome2, node_cords)
    fitness3 = fitness(new_chromosome3, node_cords)

    # Return the best candidate solution
    if fitness1 < fitness2 and fitness1 < fitness3:
        return new_chromosome1
    elif fitness2 < fitness3:
        return new_chromosome2
    else:
        return new_chromosome3
