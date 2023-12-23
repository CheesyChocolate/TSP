#!/usr/bin/env python3
import random

from module.crossover import cycle_crossover
from module.data_calculator import calculate_distance_matrix
from module.data_calculator import fitness
from module.data_calculator import combine_population_fitness
from module.file_reader import read_tsp_file
from module.file_reader import load_config
from module.local_search import two_opt as three_opt # use 2-opt while testing(can be changed to 3-opt)
from module.local_search import two_opt_random_subset
from module.mutation import generate_random_population
from module.mutation import insert_mutation
from module.mutation import random_slide_mutation
from module.selection import elitist_selection
from module.selection import rank_selection
from module.selection import roulette_selection
from module.visualization import plot_tsp_cities_dynamic
from module.visualization import plot_fitness_progress
from module.visualization import print_chromosome


def main():
    config_data = load_config()

    # get the tsp file path from the config file
    tsp_data = read_tsp_file()

    # get the coords from the tsp data
    node_cords = tsp_data['NODE_COORD_SECTION']

    # plot the cities
    figure, axis = plot_tsp_cities_dynamic(node_cords)

    # calculate the distance matrix
    distance_matrix = calculate_distance_matrix(node_cords)

    # Create the initial population
    population = generate_random_population(node_cords,
                                            config_data['population']['size'],
                                            config_data['population']['close_loop']
                                            )

    # initialize the variables
    best_chromosome = None
    consecutive_same_solution_count = 0
    best_fitness_history = []
    average_fitness_history = []
    worst_fitness_history = []

    # the genetic algorithm loop
    for generation in range(config_data['generation_count']):

        # Combine population with their respective fitness scores
        combined_data = combine_population_fitness(population, distance_matrix)

        # find the best chromosome with elitist selection
        next_population = elitist_selection(combined_data, config_data['elitist_selection_count'])
        best_chromosome = next_population[0]
        best_fitness = fitness(best_chromosome, distance_matrix)
        best_fitness_history.append(best_fitness)

        # calculate the average fitness of the population
        average_fitness = sum([fitness(chromosome, distance_matrix) for chromosome in population]) / len(population)
        average_fitness_history.append(average_fitness)

        # calculate the worst fitness of the population
        worst_fitness = min([fitness(chromosome, distance_matrix) for chromosome in population])
        worst_fitness_history.append(worst_fitness)

        # print the best chromosome
        figure, axis = plot_tsp_cities_dynamic(node_cords,
                                               best_chromosome,
                                               best_fitness,
                                               generation,
                                               figure,
                                               axis)
        print_chromosome(best_chromosome, best_fitness, generation, average_fitness, worst_fitness)

        # Generate new chromosomes for the second generation using mutation and crossover
        while len(next_population) < len(population):

            # selection
            if random.random() < config_data['rank_roulette_selection_ratio']:
                # rank selection
                parent1, parent2 = rank_selection(combined_data, 2)
            else:
                # roulette selection
                parent1, parent2 = roulette_selection(combined_data, 2)

            # crossover using cycle crossover
            child1, child2 = cycle_crossover(parent1, parent2)

            if random.random() < config_data['insert_slide_mutation_ratio']:
                child3 = insert_mutation(child1)
                child4 = insert_mutation(child2)
            else:
                child3 = random_slide_mutation(child1)
                child4 = random_slide_mutation(child2)

            # only add the best child to the next generation
            child = max([child1, child2, child3, child4], key=lambda x: fitness(x, distance_matrix))

            # apply 2-opt on the child
            if config_data['two_opt_random_subset']:
                child = two_opt_random_subset(child, distance_matrix)

            # only add the child if it is not already in the population
            if child not in next_population or config_data['allow_duplicate']:
                next_population.append(child)

        # replace the population with the new generation
        population = next_population

        # check for termination condition
        if best_fitness_history[generation] == best_fitness_history[generation - 1]:
            consecutive_same_solution_count += 1
        else:
            consecutive_same_solution_count = 0

        if consecutive_same_solution_count == config_data['consecutive_same_solution_count']:
            break

    # Plot the best chromosome of the final generation
    figure, axis = plot_tsp_cities_dynamic(node_cords,
                                           best_chromosome,
                                           best_fitness,
                                           figure=figure,
                                           axis=axis
                                           )
    print_chromosome(best_chromosome, best_fitness, generation='Final')

    print("Applyong 3-opt on the best chromosome...")

    # Apply 3-opt on the best chromosome
    best_chromosome = three_opt(best_chromosome, distance_matrix)

    # calculate the fitness of the best chromosome
    best_fitness = fitness(best_chromosome, distance_matrix)

    # Plot the best chromosome of the final generation after applying 3-opt
    plot_tsp_cities_dynamic(node_cords=node_cords,
                            chromosome=best_chromosome,
                            fitness=best_fitness,
                            Title='Best chromosome after applying 3-opt'
                            )
    print_chromosome(best_chromosome, fitness(best_chromosome, distance_matrix))

    # Plot the fitness history
    plot_fitness_progress(best_fitness_history, average_fitness_history, worst_fitness_history)


if __name__ == "__main__":
    main()
