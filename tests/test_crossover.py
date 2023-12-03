import unittest
from src.module.crossover import order_crossover


class TestOrderCrossover(unittest.TestCase):
    def test_order_crossover_closed_loop(self):
        # Test chromosomes
        parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 1]
        parent2 = [1, 7, 2, 4, 8, 5, 9, 6, 1]

        # Perform crossover
        child1, child2 = order_crossover(parent1, parent2)

        # Assert other genes in the children are unique
        child1_no_1 = child1[1:-1]
        child2_no_1 = child2[1:-1]
        self.assertEqual(len(child1_no_1), len(set(child1_no_1)))
        self.assertEqual(len(child2_no_1), len(set(child2_no_1)))
        self.assertNotEqual(child1, parent1)
        self.assertNotEqual(child2, parent2)


if __name__ == '__main__':
    unittest.main()
