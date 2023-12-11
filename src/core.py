#!/usr/bin/env python3
import sys
import random

from module.crossover import cycle_crossover
from module.data_calculator import fitness
from module.file_reader import read_tsp_file
from module.local_search import two_opt as three_opt
from module.local_search import partial_two_opt
from module.mutation import generate_random_chromosome
from module.mutation import insert_mutation
from module.mutation import random_slide_mutation
from module.selection import rank_selection
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
    coords = tsp_data['NODE_COORD_SECTION']

    # plot the cities on a graph
    plot_tsp_cities(coords)

    # Generate 100 random chromosomes and calculate their total distances
    # Create the initial population
    population = [generate_random_chromosome(coords) for _ in range(100)]

    best_chromosome = None
    consecutive_same_solution_count = 0

    for generation in range(100):
        # get the best chromosome using rank selection
        best_chromosome = rank_selection(population, tsp_data, 1)[0]

        # print the best chromosome
        print_chromosome(best_chromosome, fitness(best_chromosome, coords), generation)

        # Create the next generation
        next_generation = [best_chromosome]

        # Generate new chromosomes for the second generation using mutation and crossover
        for _ in range(99):

            # Initialize parent chromosomes
            parent_chromosome1, parent_chromosome2 = None, None

            # apply crossover
            if random.random() < 0.5:
                # use rand selection to find 2 chromosomes (50% chance)
                parent_chromosome1, parent_chromosome2 = rank_selection(population, tsp_data, 2)
            else:
                # use roulette wheel selection to find 2 chromosomes (50% chance)
                parent_chromosome1, parent_chromosome2 = roulette_selection(population, tsp_data, 2)

                # Crossover using order crossover
                new_chromosome1, new_chromosome2 = cycle_crossover(parent_chromosome1, parent_chromosome2)
                next_generation.append(new_chromosome1)
                next_generation.append(new_chromosome2)

                if random.random() < 0.5:
                    # 50% chance of using insert mutation
                    if random.random() < 0.5:
                        # use insert mutation
                        new_chromosome = insert_mutation(parent_chromosome1)
                        # apply partial 2-opt on the new chromosome
                        new_chromosome = partial_two_opt(new_chromosome, coords)
                    else:
                        # use random slide mutation
                        new_chromosome = random_slide_mutation(parent_chromosome1)
                        # apply partial 2-opt on the new chromosome
                        new_chromosome = partial_two_opt(new_chromosome, coords)

                    # add the mutation chromosome to the second generation
                    next_generation.append(new_chromosome)

        # keep only the best 100 chromosomes
        next_generation = rank_selection(next_generation, tsp_data, 100)

        # check for termination criteria
        # 1. 100 generations passed
        # 2. 5 consecutive same solutions
        if best_chromosome == next_generation[0]:
            consecutive_same_solution_count += 1
        else:
            consecutive_same_solution_count = 0

        if consecutive_same_solution_count == 5:
            break

        # Replace the current population with the next generation
        population = next_generation

    # Plot the best chromosome of the last generation
    plot_tsp_cities(coords, best_chromosome)
    print_chromosome(best_chromosome, fitness(best_chromosome, coords))

    # apply 3-opt on the best chromosome
    best_chromosome = three_opt(best_chromosome, coords)

    # Plot the best chromosome after applying 3-opt
    plot_tsp_cities(coords, best_chromosome)
    print_chromosome(best_chromosome, fitness(best_chromosome, coords))


if __name__ == "__main__":
    main()
