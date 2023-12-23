# This module contains functions for generating chromosome to the TSP problem.

# suppoted algorithms:
#   - random chromosome
#   - swap mutation
#   - inversion mutation
#   - insert mutation


import random

from .data_calculator import trim
from .data_calculator import untrim


# generate random population
# @param tsp_data: node_cords
def generate_random_population(node_cords, size=100, close_loop=True):
    population = []
    for _ in range(size):
        # Extract city IDs from the dictionary keys
        chromosome = list(node_cords.keys())
        # if a close loop is required, add the first city to the end of the chromosome
        if close_loop:
            chromosome.append(chromosome[0])
        # trim the chromosome (the trim function handles either the loop is closed or not)
        trimmed_chromosome, trimmed_gene = trim(chromosome)
        # shuffle the chromosome
        random.shuffle(trimmed_chromosome)
        # untrim the chromosome
        untrimmed_chromosome = untrim(trimmed_chromosome, trimmed_gene)
        # add the chromosome to the population
        population.append(untrimmed_chromosome)

    return population


# swap mutation
# @param chromosome: Type list
# @return: Type list
def swap_mutation(chromosome):
    trimmed_chromosome, trimmed_gene = trim(chromosome)

    # Get two distinct random positions within the trimmed chromosome
    position1, position2 = random.sample(range(len(trimmed_chromosome)), 2)

    # Swap the genes at the selected positions in the trimmed chromosome
    trimmed_chromosome[position1], trimmed_chromosome[position2] = trimmed_chromosome[position2], trimmed_chromosome[position1]

    # Untrim the trimmed chromosome to restore the start and end genes (if necessary)
    untrimmed_chromosome = untrim(trimmed_chromosome, trimmed_gene)

    return untrimmed_chromosome


# inversion mutation
# @param chromosome: Type list
# @param i: Type int
# @param k: Type int
# @return: Type list
def inversion_mutation(chromosome, i, k):
    # Trim the chromosome to preserve the initial and final genes
    trimmed_chromosome, trimmed_gene = trim(chromosome)

    # TODO: this is not a clean fix, breaks the algorithm structure
    # TODO: as a resault in an array with lenght of 9. (i, k) of (0, 8) and (1, 7) yield the same result
    # since the first gene is removed, the value of i and k should be adjusted
    if trimmed_gene:
        i -= 1
        k -= 1

        if i < 0:
            i = 0

        if k > len(trimmed_chromosome) - 1:
            k = len(trimmed_chromosome) - 1

    # Insert the sub-chromosome between the start and i
    new_chromosome = trimmed_chromosome[:i]
    # Reverse the sub-chromosome and insert it between i and k
    new_chromosome.extend(reversed(trimmed_chromosome[i:k + 1]))
    # Insert the sub-chromosome between k and the end
    new_chromosome.extend(trimmed_chromosome[k + 1:])

    # Untrim the chromosome to restore the initial and final genes
    untrimmed_chromosome = untrim(new_chromosome, trimmed_gene)

    return untrimmed_chromosome


# INSERT MUTATION
# @param chromosome: Type list
# @return: Type list
def insert_mutation(chromosome):
    # Trim the chromosome to preserve the initial and final genes
    trimmed_chromosome, trimmed_gene = trim(chromosome)

    # Select two random positions in the chromosome
    pos1, pos2 = 0, 0
    while pos1 <= pos2:
        pos1, pos2 = random.sample(range(len(trimmed_chromosome)), 2)

    # Extract the allele at pos2 and insert it after pos1, shifting all other alleles
    allele = trimmed_chromosome.pop(pos2)
    trimmed_chromosome.insert(pos1 + 1, allele)

    # Untrim the chromosome to restore the initial and final genes
    untrimmed_chromosome = untrim(trimmed_chromosome, trimmed_gene)

    return untrimmed_chromosome


# Random Slide Mutation
# TODO: same as insert mutation, but the size of the sub-chromosome is random
# @param chromosome: Type list
# @return: Type list
def random_slide_mutation(chromosome):
    # Trim the chromosome to preserve the initial and final genes
    trimmed_chromosome, trimmed_gene = trim(chromosome)

    # Select random positions in the chromosome
    pos1, pos2 = sorted(random.sample(range(len(trimmed_chromosome)), 2))

    # Extract the sub-chromosome
    sub_chromosome = trimmed_chromosome[pos1:pos2 + 1]

    # Remove the sub-chromosome from the chromosome
    trimmed_chromosome = trimmed_chromosome[:pos1] + trimmed_chromosome[pos2 + 1:]

    # Select a random position in the chromosome with max distance of 2
    pos3 = random.randint(max(0, pos1 - 2), min(len(trimmed_chromosome), pos1 + 2))

    # Insert the sub-chromosome into the chromosome
    mutated_chromosome = trimmed_chromosome[:pos3] + sub_chromosome + trimmed_chromosome[pos3:]

    # Untrim the chromosome to restore the initial and final genes
    untrimmed_chromosome = untrim(mutated_chromosome, trimmed_gene)

    return untrimmed_chromosome
