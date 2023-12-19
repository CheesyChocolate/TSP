# This module contains functions for visualizing the TSP data.
# or printing the data to the console.

# supported visualizations:
#  - plot_tsp_cities: plots the cities and the solution path (if provided)
#  - print_chromosome: prints the chromosome and its fitness to the console

import matplotlib.pyplot as plt


# @param node_cords: type node_cords dict
# @param connections: type list
# @param fitness: type float
def plot_tsp_cities(node_cords, chromosome=None, fitness=None):
    cities = node_cords
    x = [city[0] for city in cities.values()]
    y = [city[1] for city in cities.values()]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', marker='o', label='Cities')

    # If a chromosome is provided, plot the chromosome path
    if chromosome:
        chromosome_x = [cities[city_id][0] for city_id in chromosome]
        chromosome_y = [cities[city_id][1] for city_id in chromosome]
        plt.plot(chromosome_x, chromosome_y, color='red', linestyle='-', linewidth=1, alpha=0.7, label='Solution Path')

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    if fitness:
        plt.title('TSP Solution Path\nFitness: ' + str(fitness))
    else:
        plt.title('TSP Cities')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plots the progression of best fitness values across generations or iterations.
# @param fitness_values: type list
def plot_fitness_progress(fitness_values):
    generations = range(1, len(fitness_values) + 1)

    plt.figure(figsize=(8, 6))
    plt.plot(generations, fitness_values, marker='o', linestyle='-', color='blue')
    plt.xlabel('Generations/Iterations')
    plt.ylabel('Best Fitness')
    plt.title('Progression of Best Fitness')
    plt.grid(True)
    plt.show()


def print_chromosome(chromosome, fitness, generation=None):
    if generation:
        print('Generation: ', generation)

    print('Best Chromosome: ', chromosome)
    print('Fitness: ', fitness)
    print('Distance: ', 1 / fitness)
    print('-------------------------')
