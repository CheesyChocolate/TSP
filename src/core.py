#!/usr/bin/env python3
import sys
import random

from module.crossover import order_crossover
from module.data_calculator import fitness
from module.file_reader import read_tsp_file
from module.mutation import generate_random_chromosome
from module.mutation import swap_mutation
from module.selection import rank_selection
from module.selection import roulette_selection
from module.visualization import plot_tsp_cities


def main():
    # Check if the TSP file path is provided as an argument
    if len(sys.argv) > 1:
        # Get the TSP file path from the arguments
        tsp_file_path = sys.argv[1]
    else:
        # default to berlin52.tsp
        tsp_file_path = "../data/berlin52.tsp"

    tsp_data = read_tsp_file(tsp_file_path)

    # get the coords from the tsp data
    coords = tsp_data['NODE_COORD_SECTION']

    # plot the cities on a graph
    plot_tsp_cities(coords)

    # Generate 100 random chromosomes and calculate their total distances
    # Create the initial population
    population = [generate_random_chromosome(coords) for _ in range(100)]

    # get the best chromosome using rank selection
    best_chromosome = rank_selection(population, tsp_data, 1)[0]

    # print the best chromosome
    print("Best Chromosome")
    print("Path:", best_chromosome)
    print("Total Distance:", fitness(best_chromosome, coords), "\n")
    plot_tsp_cities(coords, best_chromosome)

    # add the best chromosome to the next generation
    second_generation = [best_chromosome]

    # Create 99 new chromosomes for the second generation using mutation and crossover
    for _ in range(99):
        # get the crossover probability randomly
        crossover_probability = random.random()

        # apply crossover
        if crossover_probability > 0.9:
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
            # add the mutation chromosome to the second generation
            second_generation.append(new_chromosome)

    # keep only the best 100 chromosomes
    second_generation = rank_selection(second_generation, tsp_data, 100)

    # get the best chromosome using rank selection
    best_chromosome = second_generation[0]

    # print the best chromosome
    print("Best Chromosome")
    print("Path:", best_chromosome)
    print("Total Distance:", fitness(best_chromosome, coords))
    plot_tsp_cities(coords, best_chromosome)


if __name__ == "__main__":
    main()
