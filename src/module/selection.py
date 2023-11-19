# This module contains functions for selecting chromosomes for the next generation
# suppoted algorithms:
#   - rank selection
#   - roulette wheel selection
#   - tournament selection

import random
from .data_calculator import fitness


# select chromosomes based on rank selection
# @param population: Type 2D list (chromosome: Type list)
# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @param num_selected: Type Int
# @return: new_chromosomes: Type 2D list
def rank_selection(population, tsp_data, num_selected):
    # Calculate fitness scores for each chromosome
    fitness_scores = [
        fitness(chromosome, tsp_data['NODE_COORD_SECTION'])
        for chromosome in population
    ]

    # Combine population with their respective fitness scores
    combined_data = list(zip(population, fitness_scores))

    # Sort population based on fitness scores
    sorted_chromosomes = sorted(combined_data, key=lambda x: x[1])  # Sort based on fitness scores

    # Get the top chromosomes
    top_chromosomes = [chromosome[0] for chromosome in sorted_chromosomes[:num_selected]]

    return top_chromosomes


# select chromosomes based on roulette wheel selection
# @param population: Type 2D list (chromosome: Type list)
# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @param num_selected: Type Int
# @return: selected_chromosomes: Type 2D list (chromosome x genes)
def roulette_selection(population, tsp_data, num_selected):
    # Calculate fitness scores for each chromosome
    fitness_scores = [
        fitness(chromosome, tsp_data['NODE_COORD_SECTION'])
        for chromosome in population
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
                selected_chromosomes.append(population[i])
                break

    return selected_chromosomes


# select chromosomes based on tournament selection
# @param population: Type 2D list (chromosome: Type list)
# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @param num_selected: Type Int
# @param tournament_size: Type Int
def tournament_selection(population, tsp_data, num_selected, tournament_size=3):
    selected_chromosomes = []

    while len(selected_chromosomes) < num_selected:
        # Randomly select 'tournament_size' chromosomes from the population for the tournament
        tournament_contestants = random.sample(population, tournament_size)

        # Calculate fitness scores for tournament contestants
        contestant_fitness = [
            fitness(contestant, tsp_data['NODE_COORD_SECTION'])
            for contestant in tournament_contestants
        ]

        # Select the best contestant (chromosome with the lowest fitness)
        best_contestant = tournament_contestants[contestant_fitness.index(min(contestant_fitness))]

        selected_chromosomes.append(best_contestant)

    return selected_chromosomes
