import unittest
from src.module.crossover import order_crossover


class TestMutation(unittest.TestCase):
    def test_order_crossover(self):
        # Test chromosomes
        parent1 = [1, 2, 3, 4, 5, 1]
        parent2 = [1, 4, 3, 5, 2, 1]

        # Perform crossover
        child1, child2 = order_crossover(parent1, parent2)

        # Assert '1' at the start and end of children
        self.assertEqual(child1[0], 1)
        self.assertEqual(child1[-1], 1)
        self.assertEqual(child2[0], 1)
        self.assertEqual(child2[-1], 1)

        # Assert '1' occurs exactly 2 times in the children chromosomes
        self.assertEqual(child1.count(1), 2)
        self.assertEqual(child2.count(1), 2)

        # Assert other genes in the children are unique
        child1_no_1 = child1[1:-1]
        child2_no_1 = child2[1:-1]
        self.assertEqual(len(child1_no_1), len(set(child1_no_1)))
        self.assertEqual(len(child2_no_1), len(set(child2_no_1)))


if __name__ == '__main__':
    unittest.main()
