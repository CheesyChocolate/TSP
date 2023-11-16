import unittest
from src.module.selection import rank_selection
from src.module.selection import roulette_selection
from src.module.selection import tournament_selection


class TestGeneticOperations(unittest.TestCase):

    def test_rank_selection(self):
        # Mocking chromosomes and tsp_data
        chromosomes = [
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [2, 3, 4, 1, 5],
            [3, 4, 5, 1, 2]
            # Add more chromosomes as needed
        ]

        # Mocking tsp_data (NODE_COORD_SECTION)
        tsp_data = {
            'NODE_COORD_SECTION': {
                1: (565.0, 575.0),
                2: (25.0, 185.0),
                3: (345.0, 750.0),
                4: (745.0, 225.0),
                5: (475.0, 475.0)
                # Add more city coordinates as needed
            }
        }

        # Percentage of top solutions to select
        percentage_to_select = 10  # Change this to your desired percentage

        # Test the function
        top_solutions = rank_selection(chromosomes, tsp_data, percentage_to_select)

        # Validate the output
        expected_num_selected = len(chromosomes) * percentage_to_select // 100
        self.assertEqual(len(top_solutions), expected_num_selected)
        # Ensure the selected solutions are present in the original chromosomes
        for solution in top_solutions:
            self.assertIn(solution, chromosomes)

    def test_roulette_selection(self):
        # Mocking chromosomes and tsp_data
        chromosomes = [
                [1, 2, 3, 4, 5],
                [5, 4, 3, 2, 1],
                [2, 3, 4, 1, 5],
                [3, 4, 5, 1, 2]
                # Add more chromosomes as needed
                ]

        # Mocking tsp_data (NODE_COORD_SECTION)
        tsp_data = {
                'NODE_COORD_SECTION': {
                    1: (565.0, 575.0),
                    2: (25.0, 185.0),
                    3: (345.0, 750.0),
                    4: (745.0, 225.0),
                    5: (475.0, 475.0)
                    # Add more city coordinates as needed
                    }
                }

        # Number of solutions to select
        num_selected = 2

        # Test the function
        selected_chromosomes = roulette_selection(chromosomes, tsp_data, num_selected)

        # Validate the output
        self.assertEqual(len(selected_chromosomes), num_selected)
        # Ensure the selected solutions are present in the original chromosomes
        for solution in selected_chromosomes:
            self.assertIn(solution, chromosomes)

    def test_tournament_selection(self):
        # Mocking chromosomes and tsp_data
        chromosomes = [
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [2, 3, 4, 1, 5],
            [3, 4, 5, 1, 2]
            # Add more chromosomes as needed
        ]

        # Mocking tsp_data (NODE_COORD_SECTION)
        tsp_data = {
            'NODE_COORD_SECTION': {
                1: (565.0, 575.0),
                2: (25.0, 185.0),
                3: (345.0, 750.0),
                4: (745.0, 225.0),
                5: (475.0, 475.0)
                # Add more city coordinates as needed
            }
        }

        # Number of solutions to select
        num_selected = 2

        # Test the function
        selected_chromosomes = tournament_selection(chromosomes, tsp_data, num_selected)

        # Validate the output
        self.assertEqual(len(selected_chromosomes), num_selected)
        # Ensure the selected solutions are present in the original chromosomes
        for solution in selected_chromosomes:
            self.assertIn(solution, chromosomes)


if __name__ == '__main__':
    unittest.main()
