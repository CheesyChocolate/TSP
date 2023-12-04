**NOTE:** many of my mistakes was due to the fact that I wasn't considering the
fact an array is not copied when assigned to another variable. This is a
problem because I was modifying the original array when I was assigning it to
another variable. This is why I was getting weird results.

Remember to use literal copy of arrays when needed.

# data_calculator.py

[] implement `calculate_distance_matrix` function using `scipy.spatial.distance_matrix`
[] implement `calculate_distance_matrix` function using `pandas.DataFrame`
[] implement `calculate_distance_matrix` function using `networkx.Graph`
[] store the distance matrix in a meory and use it instead of recalculating distances every time

# local_search.py

[] implement Lin–Kernighan heuristic
[] implement 3-opt with a stopping criterion

# visualization.py

[] unit tests for print_chromosome

# crossover.py

[] fix the buggy `cycle_crossover` function

# potential useful libraries

[scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance_matrix.html#scipy.spatial.distance_matrix)
[pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
[networkx](https://networkx.github.io/documentation/stable/reference/classes/graph.html)
[tqdm](https://tqdm.github.io/docs/tqdm/)
[cloudpickle](https://pypi.org/project/cloudpickle/)

https://github.com/ahmedfgad/GeneticAlgorithmPython/blob/master/pygad/visualize/plot.py
