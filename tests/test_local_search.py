import unittest

from src.module.local_search import two_opt
from src.module.local_search import partial_two_opt
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


if __name__ == '__main__':
    unittest.main()
