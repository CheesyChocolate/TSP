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

        # Sample solution (city IDs in a random order)
        solution = [3, 1, 5, 2, 4]

        # Calculate the total distance for the sample solution
        total_distance = calculate_total_distance(solution, node_coords)

        # Expected total distance for the sample solution (calculated manually)
        expected_distance = 2332.129643196118

        # Check if the calculated distance matches the expected distance (with a small tolerance)
        self.assertAlmostEqual(total_distance, expected_distance, places=5)


if __name__ == '__main__':
    unittest.main()
