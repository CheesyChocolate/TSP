# This module contains functions for generating chromosome to the TSP problem.
# suppoted algorithms:
#   - random chromosome
#   - sort and select top solutions

import random
from .data_calculator import calculate_total_distance


# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @return: Type list
def generate_random_chromosome(tsp_data):
    cities = list(tsp_data.keys())  # Extract city IDs from the dictionary keys
    cities.remove(1)  # Remove key 1 temporarily to ensure it's not in the middle of the chromosome
    random.shuffle(cities)
    # Ensure key 1 appears both at the beginning and the end of the chromosome
    chromosome = [1] + cities + [1]
    return chromosome


# @param choromosomes: Type 2D list (chromosome: Type list)
# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @param percentage: Type Int
# @return: new_chromosomes: Type 2D list
def sort_and_select_top_solutions(chromosomes, tsp_data, percentage):
    # Calculate fitness scores for each chromosome
    fitness_scores = [
        calculate_total_distance(chromosome, tsp_data['NODE_COORD_SECTION'])
        for chromosome in chromosomes
    ]

    # Combine chromosomes with their respective fitness scores
    combined_data = list(zip(chromosomes, fitness_scores))

    # Sort chromosomes based on fitness scores
    sorted_chromosomes = sorted(combined_data, key=lambda x: x[1])  # Sort based on fitness scores

    # Calculate the number of top solutions to select based on the percentage
    num_selected = int(len(chromosomes) * percentage / 100)

    # Get the top solutions
    top_solutions = [solution[0] for solution in sorted_chromosomes[:num_selected]]

    return top_solutions
