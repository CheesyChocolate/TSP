# This module is responsible for reading TSP data from files and storing it in
# a suitable data structure.
# The data structure used is a dictionary with the following keys:
#   - 'NAME': name of the problem
#   - 'COMMENT': comment about the problem
#   - 'TYPE': type of problem (TSP)
#   - 'DIMENSION': number of cities
#   - 'EDGE_WEIGHT_TYPE': type of distance between cities (EUC_2D or ATT)
#   - 'NODE_COORD_SECTION': a dictionary with the coordinates of each city
#       - key: city id
#       - value: tuple with the coordinates (x, y)

def read_tsp_file(file_path):
    tsp_data = {
        'NAME': '',
        'COMMENT': '',
        'TYPE': '',
        'DIMENSION': 0,
        'EDGE_WEIGHT_TYPE': '',
        'NODE_COORD_SECTION': {}
    }

    with open(file_path, 'r') as file:
        lines = file.readlines()
        reading_nodes = False

        for line in lines:
            line = line.strip()
            if line.startswith('NAME'):
                tsp_data['NAME'] = line.split(':')[1].strip()
            elif line.startswith('COMMENT'):
                tsp_data['COMMENT'] = line.split(':')[1].strip()
            elif line.startswith('TYPE'):
                tsp_data['TYPE'] = line.split(':')[1].strip()
            elif line.startswith('DIMENSION'):
                tsp_data['DIMENSION'] = int(line.split(':')[1].strip())
            elif line.startswith('EDGE_WEIGHT_TYPE'):
                tsp_data['EDGE_WEIGHT_TYPE'] = line.split(':')[1].strip()
            elif line.startswith('NODE_COORD_SECTION'):
                reading_nodes = True
            elif line.startswith('EOF'):
                break
            elif reading_nodes:
                city_data = line.split()
                city_id = int(city_data[0])
                x = float(city_data[1])
                y = float(city_data[2])
                tsp_data['NODE_COORD_SECTION'][city_id] = (x, y)

    return tsp_data
