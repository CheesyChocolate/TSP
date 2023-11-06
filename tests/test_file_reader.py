import unittest
from src.module.file_reader import read_tsp_file


class TestFileReader(unittest.TestCase):
    def test_read_tsp_file(self):
        file_path = 'data/berlin52.tsp'
        tsp_data = read_tsp_file(file_path)

        self.assertEqual(tsp_data['NAME'], 'berlin52')
        self.assertEqual(tsp_data['COMMENT'], '52 locations in Berlin (Groetschel)')
        self.assertEqual(tsp_data['TYPE'], 'TSP')
        self.assertEqual(tsp_data['DIMENSION'], 52)
        self.assertEqual(tsp_data['EDGE_WEIGHT_TYPE'], 'EUC_2D')
        self.assertEqual(len(tsp_data['NODE_COORD_SECTION']), 52)

        # Verify the coordinates of a few cities using city IDs as keys
        self.assertEqual(tsp_data['NODE_COORD_SECTION'][1], (565.0, 575.0))
        self.assertEqual(tsp_data['NODE_COORD_SECTION'][2], (25.0, 185.0))
        self.assertEqual(tsp_data['NODE_COORD_SECTION'][3], (345.0, 750.0))


if __name__ == '__main__':
    unittest.main()
