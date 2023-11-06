import unittest
from src.module.solution_generator import generate_random_solutions


class TestSolutionGenerator(unittest.TestCase):
    def test_generate_random_solutions(self):
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

        num_solutions = 5
        random_solutions = generate_random_solutions(tsp_data, num_solutions)

        # Ensure the correct number of solutions is generated
        self.assertEqual(len(random_solutions), num_solutions)

        # Ensure each solution has the same number of cities as in tsp_data
        num_cities = len(tsp_data['NODE_COORD_SECTION'])
        for solution in random_solutions:
            self.assertEqual(len(solution), num_cities)
            # Ensure all cities are included in the solution
            self.assertTrue(all(city in solution for city in range(num_cities)))


if __name__ == '__main__':
    unittest.main()
