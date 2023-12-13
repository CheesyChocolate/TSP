import unittest

from src.module.local_search import two_opt
from src.module.local_search import partial_two_opt
from src.module.local_search import three_opt
from src.module.data_calculator import calculate_distance_matrix
from src.module.data_calculator import fitness


class TestLocalSearch(unittest.TestCase):
    def test_two_opt(self):
        # Sample NODE_COORD_SECTION dictionary
        node_cords = {
            1: (565.0, 575.0),
            2: (25.0, 185.0),
            3: (345.0, 750.0),
            4: (745.0, 225.0),
            5: (475.0, 475.0)
        }

        # generate the matrix
        dist_matrix = calculate_distance_matrix(node_cords)

        # Sample chromosome (city IDs in a random order)
        chromosome = [1, 2, 3, 4, 5]

        # Perform the 2-opt local search
        improved_chromosome = two_opt(chromosome, dist_matrix)

        # Ensure the resulting chromosome has the same number of genes
        self.assertEqual(len(chromosome), len(improved_chromosome))

        # Calculate fitness for initial and improved chromosomes
        initial_fitness = fitness(chromosome, dist_matrix)
        improved_fitness = fitness(improved_chromosome, dist_matrix)

        # Ensure the improved solution has better fitness (lower distance)
        self.assertLess(initial_fitness, improved_fitness)

    def test_two_opt2(self):
        # Define a simple test case with a known optimal solution
        node_cords = {
            1: (0, 0),
            2: (3, 0),
            3: (3, 4),
            4: (0, 4),
            5: (1, 1)
        }

        # Initial chromosome
        chromosome = [1, 3, 2, 4, 5, 1]

        # generate the matrix
        dist_matrix = calculate_distance_matrix(node_cords)

        # Apply the partial 2-opt algorithm
        result_chromosome = two_opt(chromosome, dist_matrix)

        # Ensure the resulting chromosome has the same number of genes
        self.assertEqual(len(chromosome), len(result_chromosome))

        # Calculate fitness before and after 2-opt
        initial_fitness = fitness(chromosome, dist_matrix)
        result_fitness = fitness(result_chromosome, dist_matrix)

        # Assert that the fitness after optimization is better than before
        self.assertLess(initial_fitness, result_fitness)

    # def test_partial_two_opt(self):
    #     # Sample NODE_COORD_SECTION dictionary
    #     node_cords = {
    #         1: (565.0, 575.0),
    #         2: (25.0, 185.0),
    #         3: (345.0, 750.0),
    #         4: (745.0, 225.0),
    #         5: (475.0, 475.0),
    #         6: (685.0, 575.0),
    #         7: (685.0, 575.0),
    #         8: (685.0, 575.0)
    #     }

    #     # generate the matrix
    #     dist_matrix = calculate_distance_matrix(node_cords)

    #     # Sample chromosome (city IDs in a random order)
    #     chromosome = [7, 2, 3, 4, 5, 6, 1, 8]

    #     # Perform the 2-opt local search
    #     improved_chromosome = partial_two_opt(chromosome, dist_matrix)
    #     print(improved_chromosome)

    #     # Ensure the resulting chromosome has the same number of genes
    #     self.assertEqual(len(chromosome), len(improved_chromosome))

    #     # Calculate fitness for initial and improved chromosomes
    #     initial_fitness = fitness(chromosome, dist_matrix)
    #     improved_fitness = fitness(improved_chromosome, dist_matrix)

    #     # Ensure the improved solution has better fitness (higher fitness)
    #     self.assertLess(initial_fitness, improved_fitness)

    def test_partial_two_opt2(self):
        # Define a simple test case with a known optimal solution
        node_cords = {
            1: (0, 0),
            2: (3, 0),
            3: (3, 4),
            4: (0, 4),
            5: (1, 1)
        }

        # generate the matrix
        dist_matrix = calculate_distance_matrix(node_cords)

        # Initial chromosome
        chromosome = [1, 3, 2, 4, 5, 1]

        # Apply the partial 2-opt algorithm
        result_chromosome = partial_two_opt(chromosome, dist_matrix, max_iterations=100, fitness_threshold=0.001)

        # Ensure the resulting chromosome has the same number of genes
        self.assertEqual(len(chromosome), len(result_chromosome))

        # Calculate fitness before and after 2-opt
        initial_fitness = fitness(chromosome, dist_matrix)
        result_fitness = fitness(result_chromosome, dist_matrix)

        # Assert that the fitness after optimization is better than before
        self.assertLess(initial_fitness, result_fitness)


class TestThreeOpt(unittest.TestCase):

    def test_three_opt_basic(self):
        # Create a basic test case with a known input and expected output
        node_cords = {
            1: (0, 0),
            2: (3, 0),
            3: (3, 4),
            4: (0, 4),
            5: (1, 1),
            6: (2, 2),
            7: (1, 3),
            8: (2, 3),
            9: (1, 2)
        }

        # generate the matrix
        dist_matrix = calculate_distance_matrix(node_cords)

        chromosome = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Calculate the initial distance for comparison
        initial_fitness = fitness(chromosome, dist_matrix)

        # Apply the 3-opt algorithm
        result_chromosome = three_opt(chromosome, dist_matrix)

        # Calculate the distance of the resulting chromosome
        result_fitness = fitness(result_chromosome, dist_matrix)

        # Ensure that the resulting chromosome is different from the initial one
        self.assertNotEqual(chromosome, result_chromosome)

        # Ensure that the initial fitness is less than the resulting fitness
        self.assertLessEqual(initial_fitness, result_fitness)

        # Ensure the resulting chromosome has the same number of genes
        self.assertEqual(len(chromosome), len(result_chromosome))

        # Ensure that the resulting chromosome is a valid solution
        self.assertEqual(set(chromosome), set(result_chromosome))


if __name__ == '__main__':
    unittest.main()
