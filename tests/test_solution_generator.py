import unittest
from src.module.solution_generator import generate_random_solution


class TestSolutionGenerator(unittest.TestCase):
    def test_generate_random_solution(self):
        # Sample NODE_COORD_SECTION dictionary
        node_coords = {
            1: (565.0, 575.0),
            2: (25.0, 185.0),
            3: (345.0, 750.0),
            4: (745.0, 225.0),
            5: (475.0, 475.0)
        }

        # Generate a random solution
        random_solution = generate_random_solution(node_coords)

        num_cities = len(node_coords)
        # Ensure the solution has the correct number of cities
        # +1 for the starting city that being repeated at the end
        self.assertEqual(len(random_solution), num_cities + 1)
        # Ensure all city IDs are included in the solution
        self.assertTrue(all(city_id in random_solution for city_id in node_coords.keys()))
        # Ensure all city IDs in the solution are unique
        self.assertEqual(len(set(random_solution)), num_cities)


if __name__ == '__main__':
    unittest.main()
