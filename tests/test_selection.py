import unittest
from src.module.data_calculator import calculate_distance_matrix
from src.module.selection import rank_selection
from src.module.selection import roulette_selection
from src.module.selection import tournament_selection


class TestGeneticOperations(unittest.TestCase):

    def test_rank_selection(self):
        # Mocking population
        population = [
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [2, 3, 4, 1, 5],
            [3, 4, 5, 1, 2]
        ]

        # Mocking node_cords
        node_cords = {
            1: (565.0, 575.0),
            2: (25.0, 185.0),
            3: (345.0, 750.0),
            4: (745.0, 225.0),
            5: (475.0, 475.0)
        }

        # Number of top chromosomes to select
        num_selected = 3

        # generate the matrix
        dist_matrix = calculate_distance_matrix(node_cords)

        # Test the function
        top_chromosomes = rank_selection(population, dist_matrix, num_selected)

        # Validate the output
        self.assertEqual(len(top_chromosomes), num_selected)
        # Ensure the selected population is a subset of the original population
        for chromosome in top_chromosomes:
            self.assertIn(chromosome, population)

        # Ensure that the population is sorted
        self.assertEqual(top_chromosomes[0], [3, 4, 5, 1, 2])
        self.assertEqual(top_chromosomes[1], [2, 3, 4, 1, 5])
        self.assertEqual(top_chromosomes[2], [1, 2, 3, 4, 5])

    def test_roulette_selection(self):
        # Mocking population and node_cords
        population = [
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [2, 3, 4, 1, 5],
            [3, 4, 5, 1, 2]
        ]

        # Mocking node_cords (NODE_COORD_SECTION)
        node_cords = {
            1: (565.0, 575.0),
            2: (25.0, 185.0),
            3: (345.0, 750.0),
            4: (745.0, 225.0),
            5: (475.0, 475.0)
        }

        # Number of chromosomes to select
        num_selected = 2

        # generate the matrix
        dist_matrix = calculate_distance_matrix(node_cords)

        # Test the function
        selected_chromosomes = roulette_selection(population, dist_matrix, num_selected)

        # Validate the output
        self.assertEqual(len(selected_chromosomes), num_selected)
        # Ensure the selected population is a subset of the original population
        for chromosome in selected_chromosomes:
            self.assertIn(chromosome, population)

    def test_tournament_selection(self):
        # Mocking population and node_cords
        population = [
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [2, 3, 4, 1, 5],
            [3, 4, 5, 1, 2]
        ]

        # Mocking node_cords (NODE_COORD_SECTION)
        node_cords = {
            1: (565.0, 575.0),
            2: (25.0, 185.0),
            3: (345.0, 750.0),
            4: (745.0, 225.0),
            5: (475.0, 475.0)
        }

        # Number of chromosomes to select
        num_selected = 2

        # generate the matrix
        dist_matrix = calculate_distance_matrix(node_cords)

        # Test the function
        selected_chromosomes = tournament_selection(population, dist_matrix, num_selected)

        # Validate the output
        self.assertEqual(len(selected_chromosomes), num_selected)
        # Ensure the selected population is a subset of the original population
        for chromosome in selected_chromosomes:
            self.assertIn(chromosome, population)


if __name__ == '__main__':
    unittest.main()
