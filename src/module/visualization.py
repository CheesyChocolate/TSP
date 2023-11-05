# This module contains functions for visualizing the TSP data.
# or printing the data to the console.

import matplotlib.pyplot as plt


def plot_tsp_cities(tsp_data):
    cities = tsp_data['NODE_COORD_SECTION']
    x = [city[1] for city in cities]
    y = [city[2] for city in cities]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', marker='o', label='Cities')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('TSP Cities')
    plt.legend()
    plt.grid(True)
    plt.show()
