import sys

from module.file_reader import read_tsp_file
from module.mutation import generate_random_chromosome
from module.crossover import order_crossover
from module.selection import roulette_selection
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

    # Generate 100 random chromosomes and calculate their total distances
    chromosomes = []
    for _ in range(100):
        random_chromosome = generate_random_chromosome(tsp_data['NODE_COORD_SECTION'])
        chromosomes.append(random_chromosome)

    # find 5 chromosomes using roulette wheel selection
    selected_chromosomes = roulette_selection(chromosomes, tsp_data, 5)

    # print parent 1
    print("\nParent 1")
    print("Path:", selected_chromosomes[0])
    print("Total Distance:", fitness(selected_chromosomes[0], tsp_data['NODE_COORD_SECTION']))

    # print parent 2
    print("\nParent 2")
    print("Path:", selected_chromosomes[1])
    print("Total Distance:", fitness(selected_chromosomes[1], tsp_data['NODE_COORD_SECTION']))

    # perform order crossover
    child1, child2 = order_crossover(selected_chromosomes[0], selected_chromosomes[1])

    # print child 1
    print("\nChild 1")
    print("Path:", child1)
    print("Total Distance:", fitness(child1, tsp_data['NODE_COORD_SECTION']))
    plot_tsp_cities(tsp_data['NODE_COORD_SECTION'], child1)

    # print child 2
    print("\nChild 2")
    print("Path:", child2)
    print("Total Distance:", fitness(child2, tsp_data['NODE_COORD_SECTION']))
    plot_tsp_cities(tsp_data['NODE_COORD_SECTION'], child2)


if __name__ == "__main__":
    main()
