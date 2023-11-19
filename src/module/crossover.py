# This module contains functions for crossovering chromosomes for the next generation
# suppoted algorithms:
#   - order crossover


import random


# Order crossover
# this function heavily relies on the fact that the first and last genes of a chromosome are always '1'
# @param parent1: Type list
# @param parent2: Type list
# @return child1: Type list, Type list
def order_crossover(parent1, parent2):
    # Temporarily remove '1's from parents
    p1_start, p1_end = parent1[0], parent1[-1]
    p2_start, p2_end = parent2[0], parent2[-1]
    parent1 = parent1[1:-1]
    parent2 = parent2[1:-1]

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

    # Reinsert '1's at the start and end of children
    child1.insert(0, p1_start)
    child1.append(p1_end)
    child2.insert(0, p2_start)
    child2.append(p2_end)

    return child1, child2
