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

# Cycle crossover
# @param parent1: Type list (chromosome)
# @param parent2: Type list (chromosome)
# @return: Type tuple (child1: Type list, child2: Type list)
def cycle_crossover(original_parent1, original_parent2):
    # trim the parents
    parent1, trimmed_genes1 = trim(original_parent1)
    parent2, trimmed_genes2 = trim(original_parent2)

    # create empty children
    child1 = [None] * len(parent1)
    child2 = [None] * len(parent1)

    # cycle from the first gene
    cycle = 0
    while None in child1:
        # go through even cycles
        if cycle % 2 == 0:
            # copy a cycle from parent1 to child1 and from parent2 to child2
            start = child1.index(None)
            while True:
                child1[start] = parent1[start]
                child2[start] = parent2[start]
                start = parent1.index(parent2[start])
                # go to the next cycle if the cycle is complete
                if child1[start] is not None:
                    break
        # go through odd cycles
        else:
            # copy a cycle from parent2 to child1 and from parent1 to child2
            start = child1.index(None)
            while True:
                child1[start] = parent2[start]
                child2[start] = parent1[start]
                start = parent2.index(parent1[start])
                # go to the next cycle if the cycle is complete
                if child1[start] is not None:
                    break
        cycle += 1

    # add the first and last genes to the children
    child1 = untrim(child1, trimmed_genes1)
    child2 = untrim(child2, trimmed_genes2)

    return child1, child2
