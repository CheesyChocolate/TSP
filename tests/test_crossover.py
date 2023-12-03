import unittest
from src.module.crossover import order_crossover
from src.module.crossover import cycle_crossover


class TestOrderCrossover(unittest.TestCase):
    def test_order_crossover_closed_loop(self):
        # Test chromosomes
        original_parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 1]
        original_parent2 = [1, 7, 2, 4, 8, 5, 9, 6, 1]

        # make copies of the parents
        parent1 = original_parent1.copy()
        parent2 = original_parent2.copy()

        # Perform crossover
        child1, child2 = order_crossover(parent1, parent2)

        # Assert children are of the same length as parents
        self.assertEqual(len(child1), len(original_parent1))
        self.assertEqual(len(child2), len(original_parent2))

        # Assert other genes in the children are unique
        child1_no_1 = child1[1:-1]
        child2_no_1 = child2[1:-1]
        self.assertEqual(len(child1_no_1), len(set(child1_no_1)))
        self.assertEqual(len(child2_no_1), len(set(child2_no_1)))
        self.assertNotEqual(child1, original_parent1)
        self.assertNotEqual(child2, original_parent2)
        self.assertNotEqual(child1, original_parent2)
        self.assertNotEqual(child2, original_parent1)

    def test_order_crossover_open_loop(self):
        # Test chromosomes
        original_parent1 = [1, 2, 3, 4, 5, 6, 7, 8]
        original_parent2 = [1, 7, 2, 4, 8, 5, 9, 6]

        # make copies of the parents
        parent1 = original_parent1.copy()
        parent2 = original_parent2.copy()

        # Perform crossover
        child1, child2 = order_crossover(parent1, parent2)

        # Assert children are of the same length as parents
        self.assertEqual(len(child1), len(original_parent1))
        self.assertEqual(len(child2), len(original_parent2))

        # Assert other genes in the children are unique
        child1_no_1 = child1[1:]
        child2_no_1 = child2[1:]
        self.assertEqual(len(child1_no_1), len(set(child1_no_1)))
        self.assertEqual(len(child2_no_1), len(set(child2_no_1)))
        self.assertNotEqual(child1, original_parent1)
        self.assertNotEqual(child2, original_parent2)
        self.assertNotEqual(child1, original_parent2)
        self.assertNotEqual(child2, original_parent1)


class TestCycleCrossover(unittest.TestCase):
    def test_cycle_crossover_open_loop(self):
        # Test data for parents
        parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        parent2 = [1, 7, 2, 4, 8, 5, 9, 10, 6, 3]

        # Perform cycle crossover
        child1, child2 = cycle_crossover(parent1, parent2)

        # Assertions
        self.assertEqual(len(child1), len(parent1))
        self.assertEqual(len(child2), len(parent2))
        self.assertNotEqual(child1, parent1)
        self.assertNotEqual(child2, parent2)
        # self.assertNotEqual(child1, parent2)
        # self.assertNotEqual(child2, parent1)

    def test_cycle_crossover_open_loop_expected_outcome(self):
        # Test data for parents with a predictable outcome
        parent1 = [1, 2, 3, 4, 5]
        parent2 = [1, 3, 2, 5, 4]

        # Expected outcome for the test case
        expected_child1 = [1, 3, 2, 4, 5]
        expected_child2 = [1, 2, 3, 5, 4]

        # Perform cycle crossover
        child1, child2 = cycle_crossover(parent1, parent2)

        # Assertions
        self.assertEqual(len(child1), len(parent1))
        self.assertEqual(len(child2), len(parent2))
        self.assertEqual(child1, expected_child1)
        self.assertEqual(child2, expected_child2)

    def test_cycle_crossover_closed_loop(self):
        # Test data for parents
        parent1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
        parent2 = [1, 1, 7, 2, 4, 8, 5, 9, 10, 6, 3, 1]

        # Perform cycle crossover
        child1, child2 = cycle_crossover(parent1, parent2)

        # Assertions
        self.assertEqual(len(child1), len(parent1))
        self.assertEqual(len(child2), len(parent2))
        self.assertNotEqual(child1, parent1)
        self.assertNotEqual(child2, parent2)
        # self.assertNotEqual(child1, parent2)
        # self.assertNotEqual(child2, parent1)

    def test_cycle_crossover_closed_loop_expected_outcome(self):
        # Test data for parents with a predictable outcome
        parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        parent2 = [1, 3, 2, 5, 4, 6, 8, 7, 9, 1]

        # Expected outcome for the test case
        expected_child1 = [1, 2, 3, 5, 4, 6, 8, 7, 9, 1] # TODO: not sure if this is correct
        expected_child2 = [1, 3, 2, 4, 5, 6, 7, 8, 9, 1] # TODO: not sure if this is correct

        # Perform cycle crossover
        child1, child2 = cycle_crossover(parent1, parent2)

        # Assertions
        self.assertEqual(len(child1), len(parent1))
        self.assertEqual(len(child2), len(parent2))
        self.assertEqual(child1, expected_child1)
        self.assertEqual(child2, expected_child2)


if __name__ == '__main__':
    unittest.main()
