import sys

from module.file_reader import read_tsp_file
from module.mutation import generate_random_chromosome
from module.selection import rank_selection
from module.selection import roulette_selection
from module.selection import tournament_selection
from module.data_calculator import fitness
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
    for _ in range(100):
        random_chromosome = generate_random_chromosome(tsp_data['NODE_COORD_SECTION'])
        chromosomes.append(random_chromosome)

    # Find the 1 percent best chromosoms using tournament selection
    best_chromosomes = rank_selection(chromosomes, tsp_data, 1)

    # Print the best chromosomes and their total distances
    for i in range(len(best_chromosomes)):
        print("\nBest Solution", i + 1)
        print("Path:", best_chromosomes[i])
        print("Total Distance:", fitness(best_chromosomes[i], tsp_data['NODE_COORD_SECTION']))
        # plot_tsp_cities(tsp_data['NODE_COORD_SECTION'], best_chromosomes[i])

    # find 5 chromosomes using roulette wheel selection
    selected_chromosomes = roulette_selection(chromosomes, tsp_data, 5)

    # Print the selected chromosomes and their total distances
    for i in range(len(selected_chromosomes)):
        print("\nSelected Solution", i + 1)
        print("Path:", selected_chromosomes[i])
        print("Total Distance:", fitness(selected_chromosomes[i], tsp_data['NODE_COORD_SECTION']))
        # plot_tsp_cities(tsp_data['NODE_COORD_SECTION'], selected_chromosomes[i])

    # find 5 chromosomes using tournament selection
    selected_chromosomes = tournament_selection(chromosomes, tsp_data, 5)

    # Print the selected chromosomes and their total distances
    for i in range(len(selected_chromosomes)):
        print("\nSelected Solution", i + 1)
        print("Path:", selected_chromosomes[i])
        print("Total Distance:", fitness(selected_chromosomes[i], tsp_data['NODE_COORD_SECTION']))
        # plot_tsp_cities(tsp_data['NODE_COORD_SECTION'], selected_chromosomes[i])

if __name__ == "__main__":
    main()
