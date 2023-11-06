# This module contains functions for visualizing the TSP data.
# or printing the data to the console.

import matplotlib.pyplot as plt


# @param tsp_data: type tsp_data dict
# @param connections: type list
def plot_tsp_cities(tsp_data, solution=None):
    cities = tsp_data
    x = [city[0] for city in cities.values()]
    y = [city[1] for city in cities.values()]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', marker='o', label='Cities')

    # If a solution is provided, plot the solution path
    if solution:
        solution_x = [cities[city_id][0] for city_id in solution]
        solution_y = [cities[city_id][1] for city_id in solution]
        plt.plot(solution_x, solution_y, color='red', linestyle='-', linewidth=1, alpha=0.7, label='Solution Path')

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('TSP Cities')
    plt.legend()
    plt.grid(True)
    plt.show()
