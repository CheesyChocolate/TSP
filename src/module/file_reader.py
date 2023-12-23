# read files and configs and return data
# supported algorithms:
#   - read_tsp_file
#   - load_config
#   - find_file


# This function is responsible for reading TSP data from files and storing it in
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
def read_tsp_file(file_name=None):
    tsp_data = {
        'NAME': '',
        'COMMENT': '',
        'TYPE': '',
        'DIMENSION': 0,
        'EDGE_WEIGHT_TYPE': '',
        'NODE_COORD_SECTION': {}
    }

    if file_name is not None:
        file_path = find_file(file_name)
    else:
        file_path = find_file(load_config()['tsp_file'])
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


# This function is responsible for reading the configuration file and storing
# @return: a dictionary with the configuration
def load_config():
    import yaml

    file_path = find_file('config.yaml')
    with open(file_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config


# This function is responsible for finding the first file with the given name
# in the given directory or child directories.
# @param file_name: name of the file to be searched
# @return: the path of the file found
def find_file(file_name):
    import os

    for root, dirs, files in os.walk("."):
        for file in files:
            if file == file_name:
                return os.path.join(root, file)
    print('File not found: ' + file_name)
    print('Please, make sure the file is in the same directory or a child directory of the project root.')
    print('Exiting...')
    exit(1)
