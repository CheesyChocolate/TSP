# This module contains functions for visualizing the TSP data.
# or printing the data to the console.

# supported visualizations:
#  - plot_tsp_cities: plots the cities and the solution path (if provided)
#  - print_chromosome: prints the chromosome and its fitness to the console

import matplotlib.pyplot as plt


# @param tsp_data: type tsp_data dict
# @param connections: type list
def plot_tsp_cities(tsp_data, chromosome=None):
    cities = tsp_data
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
    plt.title('TSP Cities')
    plt.legend()
    plt.grid(True)
    plt.show()


def print_chromosome(chromosome, fitness, generation=None):
    if generation:
        print('Generation: ', generation)

    print('Best Chromosome: ', chromosome)
    print('Fitness: ', fitness)
    print('Distance: ', 1 / fitness)
    print('-------------------------')
