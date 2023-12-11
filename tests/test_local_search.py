import unittest

from src.module.local_search import two_opt
from src.module.local_search import partial_two_opt
from src.module.local_search import three_opt
from src.module.data_calculator import fitness


class TestLocalSearch(unittest.TestCase):
    def test_two_opt(self):
        # Sample NODE_COORD_SECTION dictionary
        node_coords = {
            1: (565.0, 575.0),
            2: (25.0, 185.0),
            3: (345.0, 750.0),
            4: (745.0, 225.0),
            5: (475.0, 475.0)
        }

        # Sample chromosome (city IDs in a random order)
        chromosome = [1, 2, 3, 4, 5]

        # Perform the 2-opt local search
        improved_chromosome = two_opt(chromosome, node_coords)

        # Ensure the resulting chromosome has the same number of genes
        self.assertEqual(len(chromosome), len(improved_chromosome))

        # Calculate fitness for initial and improved chromosomes
        initial_fitness = fitness(chromosome, node_coords)
        improved_fitness = fitness(improved_chromosome, node_coords)

        # Ensure the improved solution has better fitness (lower distance)
        self.assertLess(improved_fitness, initial_fitness)

    def test_two_opt2(self):
        # Define a simple test case with a known optimal solution
        node_coords = {
            1: (0, 0),
            2: (3, 0),
            3: (3, 4),
            4: (0, 4),
            5: (1, 1)
        }

        # Initial chromosome
        chromosome = [1, 3, 2, 4, 5, 1]

        # Apply the partial 2-opt algorithm
        result_chromosome = two_opt(chromosome, node_coords)

        # Ensure the resulting chromosome has the same number of genes
        self.assertEqual(len(chromosome), len(result_chromosome))

        # Calculate fitness before and after 2-opt
        initial_fitness = fitness(chromosome, node_coords)
        result_fitness = fitness(result_chromosome, node_coords)

        # Assert that the fitness after optimization is better than before
        self.assertLess(result_fitness, initial_fitness)

    def test_partial_two_opt(self):
        # Sample NODE_COORD_SECTION dictionary
        node_coords = {
            1: (565.0, 575.0),
            2: (25.0, 185.0),
            3: (345.0, 750.0),
            4: (745.0, 225.0),
            5: (475.0, 475.0)
        }

        # Sample chromosome (city IDs in a random order)
        chromosome = [1, 2, 3, 4, 5]

        # Perform the 2-opt local search
        improved_chromosome = partial_two_opt(chromosome, node_coords)

        # Ensure the resulting chromosome has the same number of genes
        self.assertEqual(len(chromosome), len(improved_chromosome))

        # Calculate fitness for initial and improved chromosomes
        initial_fitness = fitness(chromosome, node_coords)
        improved_fitness = fitness(improved_chromosome, node_coords)

        # Ensure the improved solution has better fitness (lower distance)
        self.assertLess(improved_fitness, initial_fitness)

    def test_partial_two_opt2(self):
        # Define a simple test case with a known optimal solution
        node_coords = {
            1: (0, 0),
            2: (3, 0),
            3: (3, 4),
            4: (0, 4),
            5: (1, 1)
        }
        # Initial chromosome
        chromosome = [1, 3, 2, 4, 5, 1]

        # Apply the partial 2-opt algorithm
        result_chromosome = partial_two_opt(chromosome, node_coords, max_iterations=100, fitness_threshold=0.001)

        # Ensure the resulting chromosome has the same number of genes
        self.assertEqual(len(chromosome), len(result_chromosome))

        # Calculate fitness before and after 2-opt
        initial_fitness = fitness(chromosome, node_coords)
        result_fitness = fitness(result_chromosome, node_coords)

        # Assert that the fitness after optimization is better than before
        self.assertLess(result_fitness, initial_fitness)


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
        chromosome = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Calculate the initial distance for comparison
        initial_distance = fitness(chromosome, node_cords)

        # Apply the 3-opt algorithm
        result_chromosome = three_opt(chromosome, node_cords)

        # Calculate the distance of the resulting chromosome
        result_distance = fitness(result_chromosome, node_cords)

        # Ensure that the resulting chromosome is different from the initial one
        self.assertNotEqual(chromosome, result_chromosome)

        # Ensure that the resulting distance is less than or equal to the initial distance
        self.assertLessEqual(result_distance, initial_distance)

        # Ensure the resulting chromosome has the same number of genes
        self.assertEqual(len(chromosome), len(result_chromosome))

        # Ensure that the resulting chromosome is a valid solution
        self.assertEqual(set(chromosome), set(result_chromosome))


if __name__ == '__main__':
    unittest.main()
