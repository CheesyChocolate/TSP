# This module contains functions for crossovering chromosomes for the next generation
# suppoted algorithms:
#   - order crossover
#   - cycle crossover


import random


from .data_calculator import trim
from .data_calculator import untrim


# Order crossover
# TODO: this function has the potential to create children similar to their parents
#      add a check to make sure the children are not too similar to their parents
# @param parent1: Type list
# @param parent2: Type list
# @return child1: Type list
# @return child2: Type list
def order_crossover(parent1, parent2):
    parent1, trimmed_genes1 = trim(parent1)
    parent2, trimmed_genes2 = trim(parent2)

    # Choose two random crossover points
    point1, point2 = sorted(random.sample(range(len(parent1)), 2))

    # Create copies of parents to avoid modifying them
    child1 = parent1[:]
    child2 = parent2[:]

    # Step 1: Copy the segment between the crossover points from parent1 to child1
    child1[point1:point2] = parent1[point1:point2]

    # Step 2: Copy remaining unused numbers from parent2 to child1
    idx = point2
    for gene in parent2[point2:] + parent2[:point2]:
        if gene not in child1[point1:point2]:
            child1[idx % len(parent1)] = gene
            idx += 1

    # Step 3: Create child2 by reversing the roles of parents
    child2[point1:point2] = parent2[point1:point2]
    idx = point2
    for gene in parent1[point2:] + parent1[:point2]:
        if gene not in child2[point1:point2]:
            child2[idx % len(parent2)] = gene
            idx += 1

    # Add the first and last genes to the children
    child1 = untrim(child1, trimmed_genes1)
    child2 = untrim(child2, trimmed_genes2)

    return child1, child2


# CYCLE CROSSOVER
# @param parent1: Type list
# @param parent2: Type list
# @return: Type tuple (offspring1: Type list, offspring2: Type list)
# def cycle_crossover(parent1, parent2):
#     child1 = [-1] * len(parent1)
#     child2 = [-1] * len(parent2)

#     # Initialize a list to track which elements have been visited
#     visited = [False] * len(parent1)

#     # Start the cycle crossover process
#     while True:
#         # Find the first unvisited position
#         idx = next((i for i, v in enumerate(visited) if not v), None)
#         if idx is None:
#             break  # All elements have been visited

#         # Start a new cycle
#         while not visited[idx]:
#             visited[idx] = True

#             # Assign the corresponding elements from parents to children
#             child1[idx] = parent1[idx]
#             child2[idx] = parent2[idx]

#             # Find the index of the corresponding element in the other parent
#             idx_p2 = parent1.index(parent2[idx])
#             idx = idx_p2

#     return child1, child2
