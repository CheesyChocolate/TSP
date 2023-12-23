**NOTE:** many of my mistakes was due to the fact that I wasn't considering the
fact an array is not copied when assigned to another variable. This is a
problem because I was modifying the original array when I was assigning it to
another variable. This is why I was getting weird results.

Remember to use literal copy of arrays when needed.

# other

* selection based on idea while talking with alperen, 8se push and pop
* write test unit for the remaining functions


# local_search.py

* implement Lin–Kernighan heuristic
* fix partial_two_opt unit test and uncomment it
* fix three_opt, it is putting two of first city at same position

# selection

* fix tournoment selection


# visualization.py

* unit tests for print_chromosome
* show more informatio on fitness graph(ie variance, mean, deviat)


# potential useful libraries

[tqdm](https://tqdm.github.io/docs/tqdm/)
[cloudpickle](https://pypi.org/project/cloudpickle/)
https://github.com/ahmedfgad/GeneticAlgorithmPython/blob/master/pygad/visualize/plot.py
