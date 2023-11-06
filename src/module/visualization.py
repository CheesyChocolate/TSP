# This module contains functions for visualizing the TSP data.
# or printing the data to the console.

import matplotlib.pyplot as plt


# @param tsp_data: type tsp_data dict
# @param connections: type 2D list
def plot_tsp_cities(tsp_data, connections=None):
    cities = tsp_data['NODE_COORD_SECTION']
    x = [city[1] for city in cities]
    y = [city[2] for city in cities]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', marker='o', label='Cities')

    if connections is not None:
        for connection in connections:
            plt.plot([x[connection[0]], x[connection[1]]],
                     [y[connection[0]], y[connection[1]]],
                     color='red', linestyle='-', linewidth=1, alpha=0.7)

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('TSP Cities')
    plt.legend()
    plt.grid(True)
    plt.show()
