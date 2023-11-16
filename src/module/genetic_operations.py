# This module contains functions for generating chromosome to the TSP problem.
# suppoted algorithms:
#   - random chromosome
#   - rank selection
#   - roulette wheel selection

import random
from .data_calculator import fitness


# generate random chromosome
# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @return: Type list
def generate_random_chromosome(tsp_data):
    cities = list(tsp_data.keys())  # Extract city IDs from the dictionary keys
    cities.remove(1)  # Remove key 1 temporarily to ensure it's not in the middle of the chromosome
    random.shuffle(cities)
    # Ensure key 1 appears both at the beginning and the end of the chromosome
    chromosome = [1] + cities + [1]
    return chromosome


# select chromosomes based on rank selection
# @param choromosomes: Type 2D list (chromosome: Type list)
# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @param percentage: Type Int
# @return: new_chromosomes: Type 2D list
def rank_selection(chromosomes, tsp_data, percentage):
    # Calculate fitness scores for each chromosome
    fitness_scores = [
        fitness(chromosome, tsp_data['NODE_COORD_SECTION'])
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


# select chromosomes based on roulette wheel selection
# @param chromosomes: Type 2D list (chromosome: Type list)
# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @param num_selected: Type Int
# @return: selected_chromosomes: Type 2D list (chromosome x genes)
def roulette_selection(chromosomes, tsp_data, num_selected):
    # Calculate fitness scores for each chromosome
    fitness_scores = [
        fitness(chromosome, tsp_data['NODE_COORD_SECTION'])
        for chromosome in chromosomes
    ]

    # Calculate total fitness
    total_fitness = sum(fitness_scores)

    # Calculate selection probabilities for each chromosome
    selection_probabilities = [score / total_fitness for score in fitness_scores]

    # Perform roulette wheel selection
    selected_chromosomes = []
    for _ in range(num_selected):
        # Generate a random number between 0 and 1
        rand_num = random.random()

        # Select a chromosome based on the random number using cumulative probabilities
        cumulative_prob = 0
        for i, prob in enumerate(selection_probabilities):
            cumulative_prob += prob
            if rand_num <= cumulative_prob:
                selected_chromosomes.append(chromosomes[i])
                break

    return selected_chromosomes
