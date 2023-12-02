#!/usr/bin/env python3
import sys
import random

from module.crossover import order_crossover
from module.data_calculator import fitness
from module.file_reader import read_tsp_file
from module.local_search import partial_two_opt
from module.mutation import generate_random_chromosome
from module.mutation import swap_mutation
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
        # default to berlin52.tsp
        tsp_file_path = "./data/ulysses22.tsp"

    tsp_data = read_tsp_file(tsp_file_path)

    # get the coords from the tsp data
    coords = tsp_data['NODE_COORD_SECTION']

    # plot the cities on a graph
    plot_tsp_cities(coords)

    # Generate 100 random chromosomes and calculate their total distances
    # Create the initial population
    population = [generate_random_chromosome(coords) for _ in range(100)]

    best_chromosome = None

    for generation in range(100):
        # get the best chromosome using rank selection
        best_chromosome = rank_selection(population, tsp_data, 1)[0]

        # print the best chromosome
        print_chromosome(best_chromosome, fitness(best_chromosome, coords), generation)

        # Create the next generation
        second_generation = [best_chromosome]

        # Generate new chromosomes for the second generation using mutation and crossover
        for _ in range(99):
            # get the crossover probability randomly
            crossover_probability = random.random()

            # apply crossover
            if crossover_probability > 0.4:
                # find 2 chromosomes using roulette wheel selection
                selected_chromosomes = roulette_selection(population, tsp_data, 2)
                # apply crossover
                new_chromosome1, new_chromosome2 = order_crossover(selected_chromosomes[0], selected_chromosomes[1])
                # add the crossover chromosomes to the second generation
                second_generation.append(new_chromosome1)
                second_generation.append(new_chromosome2)
            # apply mutation
            else:
                # find 1 chromosome using roulette wheel selection
                selected_chromosomes = roulette_selection(population, tsp_data, 1)
                # apply mutation
                new_chromosome = swap_mutation(selected_chromosomes[0])
                # apply 2-opt on the new chromosome
                new_chromosome = partial_two_opt(new_chromosome, coords)
                # add the mutation chromosome to the second generation
                second_generation.append(new_chromosome)

        # keep only the best 100 chromosomes
        second_generation = rank_selection(second_generation, tsp_data, 100)

        # Replace the current population with the next generation
        population = second_generation

    # Plot the best chromosome of the last generation
    plot_tsp_cities(coords, best_chromosome)

    # print the best chromosome
    print_chromosome(best_chromosome, fitness(best_chromosome, coords))

    # 2-opt on the best chromosome
    print("Applying 2-opt...")
    best_chromosome = partial_two_opt(best_chromosome, coords)

    # Plot the best chromosome after 2-opt
    plot_tsp_cities(coords, best_chromosome)

    # print the best chromosome
    print_chromosome(best_chromosome, fitness(best_chromosome, coords))


if __name__ == "__main__":
    main()
