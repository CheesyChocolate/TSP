# Description: This file contains the implementation of local search algorithm
# used to improve the solution of the genetic algorithm.

# supported algorithms:
# - 2-opt
# - 2-opt with a stopping criterion (partial 2-opt)
# - 2-opt with on a random subset
# - 3-opt

import random

from .data_calculator import fitness
from .data_calculator import trim
from .data_calculator import untrim
from .mutation import inversion_mutation


# 2-opt local search algorithm
# @param chromosome: Type list
# @param dist_matrix: type matrix
# @return: Type list
def two_opt(chromosome, dist_matrix):
    num_cities = len(chromosome)
    best_fitness = fitness(chromosome, dist_matrix)

    improved = True
    while improved:
        improved = False
        for i in range(1, num_cities - 1):
            for k in range(i + 1, num_cities):
                # Apply inversion mutation to generate a new candidate solution
                new_chromosome = inversion_mutation(chromosome, i, k)

                # Calculate the fitness of the new solution
                new_fitness = fitness(new_chromosome, dist_matrix)

                # If the new solution is better, update the chromosome and fitness
                if new_fitness > best_fitness:
                    chromosome = new_chromosome
                    best_fitness = new_fitness
                    improved = True
                    # break # uncomment these 3 lines to improve the performance
            # if improved:
            # break

    return chromosome


# 2-opt local search algorithm with a stopping criterion and a maximum number of iterations
# FUN COMMENT: Brain me BIG!!!!
# TODO: fiteness threshold can be dynamic. more iterations -> lower threshold
# @param chromosome: Type list
# @param dist_matrix: type matrix
# @param max_iterations: type int
# @param fitness_threshold: type float
# @return: Type list
def partial_two_opt(
    chromosome, dist_matrix, max_iterations=20, fitness_threshold=0.001
):
    # Initial fitness calculation
    current_fitness = fitness(chromosome, dist_matrix)
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
                new_fitness = fitness(new_chromosome, dist_matrix)

                # Calculate the improvement in fitness
                improvement = new_fitness - current_fitness

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
        current_fitness += best_improvement  # Update the current fitness

    return chromosome


# Function to optimize a random subset of given chromosome using 2-opt
# @param parent: Type list
# @param dist_matrix: type matrix
# @return: Type list
def two_opt_random_subset(parent, dist_matrix):
    chromosome, trimmed_gene = trim(parent)

    # Calculate the subset length as 38% (taken from golden ratio) of
    # chromosome length or maximum of 50
    subset_length = min(int(len(chromosome) * 0.38), 50)

    # Ensure the subset length is within bounds
    subset_length = min(subset_length, len(chromosome))

    # Select a random starting index for the subset
    start_index = random.randint(0, len(chromosome) - subset_length)

    # Extract the random subset from the chromosome
    subset = chromosome[start_index : start_index + subset_length]

    # Optimize the subset using the 2-opt algorithm
    optimized_subset = two_opt(subset, dist_matrix)

    # Replace the subset in the original chromosome with the optimized subset
    new_chromosome = (
        chromosome[:start_index]
        + optimized_subset
        + chromosome[start_index + subset_length :]
    )

    new_chromosome = untrim(new_chromosome, trimmed_gene)

    return new_chromosome


# 3-opt local search algorithm
# @param parent: Type list
# @param dist_matrix: type matrix
# @return: Type list
def three_opt(parent, dist_matrix):
    chromosome, trimmed_gene = trim(parent)

    num_cities = len(chromosome)
    best_fitness = fitness(chromosome, dist_matrix)

    improved = True
    while improved:
        improved = False
        for i in range(1, num_cities - 2):
            for j in range(i + 1, num_cities - 1):
                for k in range(j + 1, num_cities):
                    # Apply 3-opt moves to generate new candidate solutions
                    new_chromosome = three_opt_move(chromosome, dist_matrix, i, j, k)

                    # Calculate the fitness of the new solution
                    new_fitness = fitness(new_chromosome, dist_matrix)

                    # If the new solution is better, update the chromosome and distance
                    if new_fitness > best_fitness:
                        chromosome = new_chromosome
                        best_fitness = new_fitness
                        improved = True  # Set flag to continue outer loop
                        break  # Innermost loop breaks to generate new solutions
                if improved:
                    break  # Middle loop breaks if improvement occurred
            if improved:
                break  # Outer loop breaks if improvement occurred

    chromosome = untrim(chromosome, trimmed_gene)
    return chromosome


def three_opt_move(chromosome, dist_matrix, i, j, k):
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
    fitness1 = fitness(new_chromosome1, dist_matrix)
    fitness2 = fitness(new_chromosome2, dist_matrix)
    fitness3 = fitness(new_chromosome3, dist_matrix)

    # Return the best candidate solution
    if fitness1 > fitness2 and fitness1 > fitness3:
        return new_chromosome1
    elif fitness2 > fitness3:
        return new_chromosome2
    else:
        return new_chromosome3


"""

This is a very simple implementation of line segment intersection detection.
It checks every pair of edges in the TSP tour to see if they intersect.
It returns the indices of the first pair of edges that intersect.

(me stupid brain)

"""


def orientation(P, Q, R):
    """(Same as before) 0: Collinear, 1: CW, 2: CCW"""
    val = (Q[0] - P[0]) * (R[1] - P[1]) - (Q[1] - P[1]) * (R[0] - P[0])
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def on_segment(P, Q, R):
    """(Same as before) Checks if Q lies on segment PR"""
    if (
        Q[0] <= max(P[0], R[0])
        and Q[0] >= min(P[0], R[0])
        and Q[1] <= max(P[1], R[1])
        and Q[1] >= min(P[1], R[1])
    ):
        return True
    return False


def do_intersect(A, B, C, D):
    """
    Returns True ONLY if edges intersect strictly or overlapping.
    It does NOT handle the logic of shared endpoints (that is done in the loop).
    """
    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)
    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)

    # General Case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases (Collinear)
    if o1 == 0 and on_segment(A, C, B):
        return True
    if o2 == 0 and on_segment(A, D, B):
        return True
    if o3 == 0 and on_segment(C, A, D):
        return True
    if o4 == 0 and on_segment(C, B, D):
        return True

    return False


def find_first_intersection(chromosome, node_cords):
    """
    Scans a TSP tour for the FIRST intersection found.

    Args:
        chromosome: A list of node IDs representing the tour order.
                    Example: [1, 3, 2, 4, 5, 1]
        node_cords: A dictionary mapping node IDs to (x, y) coordinates.
                    Example: {1: (0, 0), 2: (3, 0), 3: (3, 4), ...}
    Returns:
        Tuple (i, j) of edge indices that intersect, or None if no intersections.
        Edge i connects chromosome[i] -> chromosome[i+1]
        Edge j connects chromosome[j] -> chromosome[j+1]
    """
    # Convert chromosome (node IDs) to coordinate tour
    tour = [node_cords[node_id] for node_id in chromosome]
    n = len(tour)

    # Loop through every edge in the tour
    for i in range(n - 1):
        # Loop through edges ahead of i
        # We start at i + 2 to skip the immediate next edge (adjacent)
        for j in range(i + 2, n - 1):
            # Skip if edges are adjacent (share a node)
            if j == i + 1:
                continue

            # Define the points for Edge 1 (connects i to i+1)
            p1 = tour[i]
            q1 = tour[i + 1]

            # Define the points for Edge 2 (connects j to j+1)
            p2 = tour[j]
            q2 = tour[j + 1]

            if do_intersect(p1, q1, p2, q2):
                return (i, j)

    return None


def untangle_with_partial_two_opt(chromosome, node_cords, dist_matrix, max_iterations=20):
    """
    Detects the first crossing and uses a 2-opt move (reversal) to untangle it.
    
    Args:
        chromosome: A list of node IDs representing the tour order.
        node_cords: A dictionary mapping node IDs to (x, y) coordinates.
        dist_matrix: Distance matrix for fitness calculation (unused but kept for API consistency).
        max_iterations: Unused, kept for API consistency.
    Returns:
        The untangled chromosome, or original if no crossings found.
    """
    intersection = find_first_intersection(chromosome, node_cords)
    
    if intersection is None:
        return chromosome  # No crossings found
    
    i, j = intersection
    
    # Apply 2-opt move: reverse the segment between i+1 and j (inclusive)
    # This removes the crossing by reversing the path between the intersecting edges
    untangled = chromosome[:i + 1] + chromosome[i + 1:j + 1][::-1] + chromosome[j + 1:]
    
    return untangled
