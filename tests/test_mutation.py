import unittest

from src.module.mutation import generate_random_chromosome
from src.module.mutation import swap_mutation


class TestMutation(unittest.TestCase):

    def test_generate_random_chromosome(self):
        # Sample NODE_COORD_SECTION dictionary
        node_coords = {
            1: (565.0, 575.0),
            2: (25.0, 185.0),
            3: (345.0, 750.0),
            4: (745.0, 225.0),
            5: (475.0, 475.0)
        }

        # Generate a random chromosome
        random_chromosome = generate_random_chromosome(node_coords)

        num_cities = len(node_coords)
        # Ensure the chromosome has the correct number of cities
        # +1 for the starting city that being repeated at the end
        self.assertEqual(len(random_chromosome), num_cities + 1)
        # Ensure all city IDs are included in the chromosome
        self.assertTrue(all(city_id in random_chromosome for city_id in node_coords.keys()))
        # Ensure all city IDs in the chromosome are unique
        self.assertEqual(len(set(random_chromosome)), num_cities)

    def test_swap_mutation(self):
        # Test swap mutation on a chromosome with start and end genes the same
        chromosome = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        mutated_chromosome = swap_mutation(chromosome)

        # Ensure the chromosome length remains the same
        self.assertEqual(len(mutated_chromosome), len(chromosome))

        # Ensure start and end genes remain the same if they were identical
        if chromosome[0] == chromosome[-1]:
            self.assertEqual(mutated_chromosome[0], chromosome[0])
            self.assertEqual(mutated_chromosome[-1], chromosome[-1])

        # Ensure that the rest of the genes have been shuffled properly
        self.assertNotEqual(mutated_chromosome[1:-1], chromosome[1:-1])
        # Additional assertions based on specific scenarios or requirements


if __name__ == '__main__':
    unittest.main()
