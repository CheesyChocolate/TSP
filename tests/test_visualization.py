import unittest
from unittest.mock import patch
from src.module.visualization import plot_tsp_cities


class TestVisualization(unittest.TestCase):
    def test_plot_tsp_cities(self):
        tsp_data = {
            'NODE_COORD_SECTION': [(1, 565.0, 575.0), (2, 25.0, 185.0), (3, 345.0, 750.0)]
        }

        with patch('src.module.visualization.plt.show') as mock_show:
            plot_tsp_cities(tsp_data)

        # Assert that plt.show() was called
        mock_show.assert_called_once()


if __name__ == '__main__':
    unittest.main()
