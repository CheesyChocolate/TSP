import unittest
from src.module.data_calculator import calculate_total_distance


class TestDataCalculator(unittest.TestCase):
    def test_calculate_total_distance(self):
        # Sample NODE_COORD_SECTION dictionary
        node_coords = {
            1: (565.0, 575.0),
            2: (25.0, 185.0),
            3: (345.0, 750.0),
            4: (745.0, 225.0),
            5: (475.0, 475.0)
        }

        # Sample chromosome (city IDs in a random order)
        chromosome = [3, 1, 5, 2, 4]

        # Calculate the total distance for the sample chromosome
        total_distance = calculate_total_distance(chromosome, node_coords)

        # Expected total distance for the sample chromosome (calculated manually)
        expected_distance = 1672.110704073914

        # Check if the calculated distance matches the expected distance (with a small tolerance)
        self.assertAlmostEqual(total_distance, expected_distance, places=5)


if __name__ == '__main__':
    unittest.main()
