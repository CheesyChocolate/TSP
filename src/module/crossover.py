# This module contains functions for crossovering chromosomes for the next generation
# suppoted algorithms:
#   - order crossover
#   - cycle crossover


import random


from .data_calculator import trim
from .data_calculator import untrim


# Order crossover
# this function heavily relies on the fact that the first and last genes of a chromosome are always '1'
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
# TODO: this implementation is messy, fails the commented test case and out
# right does not function as expected
# @param parent1: Type list (chromosome)
# @param parent2: Type list (chromosome)
# @return: Type list (offspring1)
# @return: Type list (offspring2)
def cycle_crossover(parent1, parent2):
    # Trin the first and last genes of the chromosome
    parent1, trimmed_genes1 = trim(parent1)
    parent2, trimmed_genes2 = trim(parent2)

    # TODO: a hacky fix, need to be fixed
    # if there exist a trimmed_gene1 and trimmed_gene2, then
    # shift all the values in parent1 and parent2 to the right by -1
    if trimmed_genes1 and trimmed_genes2:
        for i in range(len(parent1)):
            parent1[i] = parent1[i] - 1
            parent2[i] = parent2[i] - 1

    allele_count = len(parent1)
    flags = [False] * allele_count
    ht1 = {}
    for j in range(allele_count):
        temp_pair = {
            'value2': parent2[j],
            'index2': j,
            'value1': parent1[j]
        }
        ht1[parent2[j]] = temp_pair

    cycles = []
    for j in range(allele_count):
        temp_cycle = []
        if not flags[j]:
            cycle_start = j
            temp_pair = ht1[parent1[cycle_start]]
            temp_cycle.append(temp_pair)
            flags[temp_pair['index2']] = True
            while temp_pair['index2'] != cycle_start:
                temp_pair = ht1[parent1[temp_pair['index2']]]
                temp_cycle.append(temp_pair)
                flags[temp_pair['index2']] = True
            cycles.append(temp_cycle)

    child1 = [-1] * allele_count
    child2 = [-1] * allele_count
    counter = 0
    for cycle in cycles:
        for temp_pair in cycle:
            if counter % 2 == 0:
                child1[temp_pair['index2']] = temp_pair['value1']
                child2[temp_pair['index2']] = temp_pair['value2']
            else:
                child1[temp_pair['index2']] = temp_pair['value2']
                child2[temp_pair['index2']] = temp_pair['value1']
        counter += 1

    # TODO: a hacky fix, need to be fixed
    # if there exist a trimmed_gene1 and trimmed_gene2, then
    # shift all the values in child1 and child2 to the right by +1
    if trimmed_genes1 and trimmed_genes2:
        for i in range(len(child1)):
            child1[i] = child1[i] + 1
            child2[i] = child2[i] + 1

    # Add the first and last genes to the children
    child1 = untrim(child1, trimmed_genes1)
    child2 = untrim(child2, trimmed_genes2)

    return child1, child2
