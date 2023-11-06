import sys

from module.file_reader import read_tsp_file
from module.solution_generator import generate_random_solution
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

    # Plot TSP nodes before generating random solution
    plot_tsp_cities(tsp_data['NODE_COORD_SECTION'])

    # Generate 20 random solutions and calculate their total distances
    solutions = []
    for _ in range(20):
        random_solution = generate_random_solution(tsp_data['NODE_COORD_SECTION'])
        total_distance = calculate_total_distance(random_solution, tsp_data['NODE_COORD_SECTION'])
        solutions.append((random_solution, total_distance))

    # Sort solutions based on total distance and find the best two solutions
    solutions.sort(key=lambda x: x[1])
    best_solution_1, distance_1 = solutions[0]
    best_solution_2, distance_2 = solutions[1]

    # Print the best two solutions and their total distances
    print("\nBest Solution 1:")
    print("Path:", best_solution_1)
    print("Total Distance:", distance_1)

    print("\nBest Solution 2:")
    print("Path:", best_solution_2)
    print("Total Distance:", distance_2)

    # Plot the best two solutions
    print("\nPlotting the best two solutions:")
    plot_tsp_cities(tsp_data['NODE_COORD_SECTION'], best_solution_1)
    plot_tsp_cities(tsp_data['NODE_COORD_SECTION'], best_solution_2)


if __name__ == "__main__":
    main()
