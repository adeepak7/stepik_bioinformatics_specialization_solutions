from .hamming_distance import find_hamming_distance

dp_map_that_stores_all_neighbors_with_expected_hamming_distance = {}

unique_nucleotides = {'A', 'C', 'G', 'T'}


def suffix(pattern):
    if len(pattern) <= 1:
        return None
    else:
        return pattern[1: (len(pattern))]


def first_symbol(pattern):
    if len(pattern) == 0:
        return None
    else:
        return pattern[0]


def find_neighbors_with_expected_hamming_distance(pattern, expected_hamming_distance):

    if expected_hamming_distance == 0:
        return {pattern}

    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    if (pattern, expected_hamming_distance) in dp_map_that_stores_all_neighbors_with_expected_hamming_distance.keys():
        return dp_map_that_stores_all_neighbors_with_expected_hamming_distance[(pattern, expected_hamming_distance)]

    neighborhood_set = set()

    suffix_neighbors_set = find_neighbors_with_expected_hamming_distance(suffix(pattern), expected_hamming_distance)

    for suffix_neighbor in suffix_neighbors_set:

        if find_hamming_distance(suffix(pattern), suffix_neighbor) < expected_hamming_distance:

            for nucleotide in unique_nucleotides:
                neighborhood_set.add(nucleotide + suffix_neighbor)

        else:
            neighborhood_set.add(first_symbol(pattern) + suffix_neighbor)

    if (pattern, expected_hamming_distance) not in dp_map_that_stores_all_neighbors_with_expected_hamming_distance.keys():
        dp_map_that_stores_all_neighbors_with_expected_hamming_distance[
            (pattern, expected_hamming_distance)] = neighborhood_set

    return neighborhood_set
