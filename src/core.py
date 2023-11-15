import sys

from module.file_reader import read_tsp_file
from module.genetic_operations import generate_random_chromosome
from module.data_calculator import calculate_total_distance
from module.visualization import plot_tsp_cities


def main():
    # Check if the TSP file path is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python core.py <TSP_FILE_PATH>")
        return

    # Get the TSP file path from the command-line argument
    tsp_file_path = sys.argv[1]

    # Read TSP data from the file
    tsp_data = read_tsp_file(tsp_file_path)

    # Plot TSP nodes before generating random chromosome
    plot_tsp_cities(tsp_data['NODE_COORD_SECTION'])

    # Generate 20 random chromosomes and calculate their total distances
    chromosomes = []
    for _ in range(20):
        random_chromosome = generate_random_chromosome(tsp_data['NODE_COORD_SECTION'])
        total_distance = calculate_total_distance(random_chromosome, tsp_data['NODE_COORD_SECTION'])
        chromosomes.append((random_chromosome, total_distance))

    # Sort chromosomes based on total distance and find the best two chromosomes
    chromosomes.sort(key=lambda x: x[1])
    best_chromosome_1, distance_1 = chromosomes[0]
    best_chromosome_2, distance_2 = chromosomes[1]

    # Print the best two chromosomes and their total distances
    print("\nBest Solution 1:")
    print("Path:", best_chromosome_1)
    print("Total Distance:", distance_1)

    print("\nBest Solution 2:")
    print("Path:", best_chromosome_2)
    print("Total Distance:", distance_2)

    # Plot the best two chromosomes
    print("\nPlotting the best two chromosomes:")
    plot_tsp_cities(tsp_data['NODE_COORD_SECTION'], best_chromosome_1)
    plot_tsp_cities(tsp_data['NODE_COORD_SECTION'], best_chromosome_2)


if __name__ == "__main__":
    main()
