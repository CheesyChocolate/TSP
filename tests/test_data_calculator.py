import unittest

from src.module.data_calculator import fitness
from src.module.data_calculator import trim
from src.module.data_calculator import untrim


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
        total_distance = fitness(chromosome, node_coords)

        # Expected total distance for the sample chromosome (calculated manually)
        expected_distance = 1672.110704073914

        # Check if the calculated distance matches the expected distance (with a small tolerance)
        self.assertAlmostEqual(total_distance, expected_distance, places=5)

    def test_trim_same_first_last_genes(self):
        # Test trimming when first and last genes are the same
        chromosome = [1, 2, 3, 4, 1]
        trimmed_chromosome, trimmed_gene = trim(chromosome)
        self.assertEqual(trimmed_chromosome, [2, 3, 4])
        self.assertEqual(trimmed_gene, 1)

    def test_trim_different_first_last_genes(self):
        # Test trimming when first and last genes are different
        chromosome = [1, 2, 3, 4, 5]
        trimmed_chromosome, trimmed_gene = trim(chromosome)
        self.assertEqual(trimmed_chromosome, [1, 2, 3, 4, 5])
        self.assertEqual(trimmed_gene, None)

    def test_untrim(self):
        # Test untrimming the trimmed chromosome
        trimmed_chromosome = [2, 3, 4]
        trimed_gene = 9
        untrimmed_chromosome = untrim(trimmed_chromosome, trimed_gene)
        self.assertEqual(untrimmed_chromosome, [9, 2, 3, 4, 9])


if __name__ == '__main__':
    unittest.main()
