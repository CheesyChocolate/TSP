# This module contains functions for generating chromosome to the TSP problem.

# suppoted algorithms:
#   - random chromosome
#   - swap mutation
#   - inversion mutation
#   - insert mutation


import random


from .data_calculator import trim
from .data_calculator import untrim


# generate random chromosome
# @param tsp_data: Type dict (NODE_COORD_SECTION)
# @return: Type list
def generate_random_chromosome(tsp_data, close_loop=True):
    # Extract city IDs from the dictionary keys
    chromosome = list(tsp_data.keys())
    # if a close loop is required, add the first city to the end of the chromosome
    if close_loop:
        chromosome.append(chromosome[0])
    # trim the chromosome (the trim function handles either the loop is closed or not)
    trimmed_chromosome, trimmed_gene = trim(chromosome)
    # shuffle the chromosome
    random.shuffle(trimmed_chromosome)
    # untrim the chromosome
    untrimmed_chromosome = untrim(trimmed_chromosome, trimmed_gene)
    return untrimmed_chromosome


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
# TODO: this function has a chance to generate a child similar to the parent
#    this is because the subsequence can be shifted to the same position
#    this can be fixed by checking if the subsequence is shifted to the same position
# @param chromosome: Type list
# @return: Type list
def random_slide_mutation(chromosome):
    # Get the length of the chromosome
    chrom_length = len(chromosome)

    # Define the range for the subsequence to be shifted
    start_idx = 0
    end_idx = 0

    # ensure that the subsequence is at least 2 genes long
    while end_idx - start_idx < 2:
        start_idx = random.randint(0, chrom_length - 1)
        end_idx = random.randint(start_idx + 1, chrom_length)

    # Get the subsequence to be shifted
    subsequence = chromosome[start_idx:end_idx]

    # Remove the subsequence from the chromosome
    del chromosome[start_idx:end_idx]

    # Determine the random position for insertion
    insert_idx = random.randint(0, chrom_length - len(subsequence))

    # Insert the subsequence at the random position
    chromosome[insert_idx:insert_idx] = subsequence

    return chromosome
