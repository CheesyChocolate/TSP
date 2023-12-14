#!/usr/bin/env python3
import sys
import random

from module.crossover import cycle_crossover
from module.data_calculator import calculate_distance_matrix
from module.data_calculator import fitness
from module.data_calculator import combine_population_fitness
from module.file_reader import read_tsp_file
from module.local_search import two_opt as three_opt
from module.local_search import two_opt
from module.mutation import generate_random_chromosome
from module.mutation import insert_mutation
from module.mutation import random_slide_mutation
from module.selection import elitist_selection
from module.selection import elitist_selection as rank_selection
from module.selection import roulette_selection
from module.visualization import plot_tsp_cities
from module.visualization import print_chromosome


def main():
    # Check if the TSP file path is provided as an argument
    if len(sys.argv) > 1:
        # Get the TSP file path from the arguments
        tsp_file_path = sys.argv[1]
    else:
        print("Please provide the TSP file path as an argument.")
        print("Example: python3 core.py <TSP file path>")
        exit(1)

    tsp_data = read_tsp_file(tsp_file_path)

    # get the coords from the tsp data
    node_cords = tsp_data['NODE_COORD_SECTION']

    # calculate the distance matrix
    distance_matrix = calculate_distance_matrix(node_cords)

    # plot the cities on a graph
    plot_tsp_cities(node_cords)

    # Create the initial population
    population = [generate_random_chromosome(node_cords) for _ in range(100)]

    best_chromosome = None
    consecutive_same_solution_count = 0

    for generation in range(100):

        # Combine population with their respective fitness scores
        combined_data = combine_population_fitness(population, distance_matrix)

        # find the best chromosome with elitist selection
        best_chromosome = elitist_selection(combined_data, 1)[0]
        best_fitness = fitness(best_chromosome, distance_matrix)

        # print the best chromosome
        print_chromosome(best_chromosome, best_fitness, generation)

        # create the next generation
        next_population = [best_chromosome]

        # Generate new chromosomes for the second generation using mutation and crossover
        while len(next_population) < len(population):

            # selection
            if random.random() < 0.5:
                # rank selection
                parent1, parent2 = rank_selection(combined_data, 2)
            else:
                # roulette selection
                parent1, parent2 = roulette_selection(combined_data, 2)

            # crossover using cycle crossover
            child1, child2 = cycle_crossover(parent1, parent2)
            next_population.append(child1)
            next_population.append(child2)

            if random.random() < 0.5:
                child1 = insert_mutation(child1)
                child1 = two_opt(child1, distance_matrix)
            else:
                child1 = random_slide_mutation(child1)
                child1 = two_opt(child1, distance_matrix)

            # add the mutated child to the next population
            next_population.append(child1)

            # check for termination condition
            if best_chromosome == next_population[0]:
                consecutive_same_solution_count += 1
            else:
                consecutive_same_solution_count = 0

            if consecutive_same_solution_count == 5:
                break

            # replace the population with the new generation
            population = next_population

    # Plot the best chromosome of the final generation
    plot_tsp_cities(node_cords, best_chromosome)
    print_chromosome(best_chromosome, best_fitness)

    print("Applyong 3-opt on the best chromosome...")

    # Apply 3-opt on the best chromosome
    best_chromosome = three_opt(best_chromosome, distance_matrix)

    # Plot the best chromosome of the final generation
    plot_tsp_cities(node_cords, best_chromosome)
    print_chromosome(best_chromosome, fitness(best_chromosome, distance_matrix))



if __name__ == "__main__":
    main()
