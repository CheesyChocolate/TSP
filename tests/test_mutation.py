import unittest

from src.module.mutation import generate_random_population
from src.module.mutation import swap_mutation
from src.module.mutation import inversion_mutation
from src.module.mutation import insert_mutation
from src.module.mutation import random_slide_mutation


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
        random_chromosome = generate_random_population(node_coords, 1)[0]

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

        # Ensure that the rest of the genes have been shuffled properly
        self.assertNotEqual(mutated_chromosome[1:-1], chromosome[1:-1])

        # ensure there's no repeated gene except the start/end gene
        # first remove the start/end gene from the mutated chromosome
        mutated_chromosome = mutated_chromosome[1:-1]
        self.assertEqual(len(set(mutated_chromosome)), len(mutated_chromosome))

    def test_inversion_mutation1(self):
        # Create a sample chromosome
        chromosome = [1, 2, 3, 4, 5, 6, 7, 8, 1]  # Assuming the chromosome starts and ends with 1

        # Apply inversion mutation on a specific segment (e.g., indices 2 to 6)
        mutated_chromosome = inversion_mutation(chromosome, 2, 6)
        # Define the expected result after inversion mutation
        expected_result = [1, 2, 7, 6, 5, 4, 3, 8, 1]  # Expected result after inverting indices 2 to 6
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # Apply inversion mutation on a specific segment (e.g., indices 0 to 8)
        mutated_chromosome = inversion_mutation(chromosome, 0, 8)
        # Define the expected result after inversion mutation
        expected_result = [1, 8, 7, 6, 5, 4, 3, 2, 1]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # Apply inversion mutation on a specific segment (e.g., indices 1 to 7)
        mutated_chromosome = inversion_mutation(chromosome, 1, 7)
        # Define the expected result after inversion mutation
        expected_result = [1, 8, 7, 6, 5, 4, 3, 2, 1]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # Apply inversion mutation on a specific segment (e.g., indices 3 to 5)
        mutated_chromosome = inversion_mutation(chromosome, 3, 5)
        # Define the expected result after inversion mutation
        expected_result = [1, 2, 3, 6, 5, 4, 7, 8, 1]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # Apply inversion mutation on a specific segment (e.g., indices 4 to 4)
        mutated_chromosome = inversion_mutation(chromosome, 4, 4)
        # Define the expected result after inversion mutation
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 1]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # apply inversion mutation on a specific segment (e.g., indices 0 to 3)
        mutated_chromosome = inversion_mutation(chromosome, 0, 3)
        # Define the expected result after inversion mutation
        expected_result = [1, 4, 3, 2, 5, 6, 7, 8, 1]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # apply inversion mutation on a specific segment (e.g., indices 5 to 8)
        mutated_chromosome = inversion_mutation(chromosome, 5, 8)
        # Define the expected result after inversion mutation
        expected_result = [1, 2, 3, 4, 5, 8, 7, 6, 1]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

    def test_inversion_mutation2(self):
        # Create a sample chromosome
        chromosome = [1, 2, 3, 4, 5, 6, 7, 8]

        # Apply inversion mutation on a specific segment (e.g., indices 2 to 6)
        mutated_chromosome = inversion_mutation(chromosome, 2, 6)
        # Define the expected result after inversion mutation
        expected_result = [1, 2, 7, 6, 5, 4, 3, 8]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # Apply inversion mutation on a specific segment (e.g., indices 0 to 7)
        mutated_chromosome = inversion_mutation(chromosome, 0, 7)
        # Define the expected result after inversion mutation
        expected_result = [8, 7, 6, 5, 4, 3, 2, 1]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # Apply inversion mutation on a specific segment (e.g., indices 1 to 6)
        mutated_chromosome = inversion_mutation(chromosome, 1, 6)
        # Define the expected result after inversion mutation
        expected_result = [1, 7, 6, 5, 4, 3, 2, 8]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # Apply inversion mutation on a specific segment (e.g., indices 3 to 5)
        mutated_chromosome = inversion_mutation(chromosome, 3, 5)
        # Define the expected result after inversion mutation
        expected_result = [1, 2, 3, 6, 5, 4, 7, 8]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # Apply inversion mutation on a specific segment (e.g., indices 4 to 4)
        mutated_chromosome = inversion_mutation(chromosome, 4, 4)
        # Define the expected result after inversion mutation
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)

        # apply inversion mutation on a specific segment (e.g., indices 3 to 7)
        mutated_chromosome = inversion_mutation(chromosome, 3, 7)
        # Define the expected result after inversion mutation
        expected_result = [1, 2, 3, 8, 7, 6, 5, 4]
        # Assert that the mutation produces the expected result
        self.assertEqual(mutated_chromosome, expected_result)


class TestInsertMutation(unittest.TestCase):
    def test_open_loop_insert_mutation(self):
        # Test for open loop mutation (without start and end genes being the same)
        original_chromosome = [1, 2, 3, 4, 5]
        chromosome = original_chromosome.copy()

        mutated_chromosome = insert_mutation(chromosome)

        # Assert that the length remains the same
        self.assertEqual(len(original_chromosome), len(mutated_chromosome))

        # Assert that the chromosomes are different
        self.assertNotEqual(original_chromosome, mutated_chromosome)

        # ensure there's no repeated gene
        self.assertEqual(len(set(mutated_chromosome)), len(mutated_chromosome))

    def test_closed_loop_insert_mutation(self):
        # Test for closed loop mutation (start and end genes being the same)
        original_chromosome = [1, 2, 3, 4, 5, 1]
        chromosome = original_chromosome.copy()

        mutated_chromosome = insert_mutation(chromosome)

        # Assert that the length remains the same
        self.assertEqual(len(original_chromosome), len(mutated_chromosome))

        # Assert that the chromosomes are different
        self.assertNotEqual(original_chromosome, mutated_chromosome)

        # ensure the only repeated gene is the start/end gene
        # first remove the start/end gene from the mutated chromosome
        mutated_chromosome = mutated_chromosome[1:-1]
        self.assertEqual(len(set(mutated_chromosome)), len(mutated_chromosome))


class TestRandomSlideMutation(unittest.TestCase):
    def test_open_loop_random_slide_mutation(self):
        # Test for open loop mutation (without start and end genes being the same)
        original_chromosome = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        chromosome = original_chromosome.copy()

        mutated_chromosome = random_slide_mutation(chromosome)

        print(original_chromosome)
        print(mutated_chromosome)

        # Assert that the length remains the same
        self.assertEqual(len(original_chromosome), len(mutated_chromosome))

        # ensure there's no repeated gene
        self.assertEqual(len(set(mutated_chromosome)), len(mutated_chromosome))

        # Assert that the chromosomes are different
        # self.assertNotEqual(original_chromosome, mutated_chromosome) #TODO: This assertion fails sometimes

    def test_closed_loop_random_slide_mutation(self):
        # Test for closed loop mutation (start and end genes being the same)
        original_chromosome = [1, 2, 3, 4, 5, 6, 7, 8, 1]
        chromosome = original_chromosome.copy()

        # ensure the only repeated gene is the start/end gene
        self.assertEqual(len(set(chromosome)), len(chromosome) - 1)

        mutated_chromosome = random_slide_mutation(chromosome)

        # Assert that the length remains the same
        self.assertEqual(len(original_chromosome), len(mutated_chromosome))

        # ensure the only repeated gene is the start/end gene
        # first remove the start/end gene from the mutated chromosome
        mutated_chromosome = mutated_chromosome[1:-1]
        self.assertEqual(len(set(mutated_chromosome)), len(mutated_chromosome))

        # Assert that the chromosomes are different
        # self.assertNotEqual(original_chromosome, mutated_chromosome) # TODO: This assertion fails sometimes


if __name__ == '__main__':
    unittest.main()
