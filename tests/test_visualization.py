import unittest
from unittest.mock import patch
from src.module.visualization import plot_tsp_cities


class TestVisualization(unittest.TestCase):
    def setUp(self):
        # Sample NODE_COORD_SECTION dictionary
        self.tsp_data = {
            1: (565.0, 575.0),
            2: (25.0, 185.0),
            3: (345.0, 750.0),
            4: (745.0, 225.0),
            5: (475.0, 475.0)
        }

        # Sample chromosome (city IDs in a specific order)
        self.chromosome = [1, 3, 2, 5, 4]

    @patch('src.module.visualization.plt.show')  # Mocking plt.show() method
    def test_plot_tsp_cities_with_chromosome(self, mock_show):
        # Test plotting cities with a chromosome
        plot_tsp_cities(self.tsp_data, self.chromosome)

        # Assert that plt.show() was called once
        mock_show.assert_called_once()

    @patch('src.module.visualization.plt.show')  # Mocking plt.show() method
    def test_plot_tsp_cities_without_chromosome(self, mock_show):
        # Test plotting cities without a chromosome
        plot_tsp_cities(self.tsp_data)

        # Assert that plt.show() was called once
        mock_show.assert_called_once()


if __name__ == '__main__':
    unittest.main()
