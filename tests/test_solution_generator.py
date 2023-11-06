import unittest
from src.module.solution_generator import generate_random_solution


class TestSolutionGenerator(unittest.TestCase):
    def test_generate_random_solution(self):
        # Create a sample tsp_data
        tsp_data = {
            'NODE_COORD_SECTION': [
                (0, 565.0, 575.0),
                (1, 25.0, 185.0),
                (2, 345.0, 750.0),
                (3, 745.0, 225.0),
                (4, 475.0, 475.0)
            ]
        }

        # Generate a random solution
        random_solution = generate_random_solution(tsp_data)

        num_cities = len(tsp_data['NODE_COORD_SECTION'])
        # Ensure the solution has the correct number of cities
        self.assertEqual(len(random_solution[0]), num_cities)
        # Ensure all cities are included in the solution
        self.assertTrue(all(city in random_solution[0] for city in range(num_cities)))


if __name__ == '__main__':
    unittest.main()
