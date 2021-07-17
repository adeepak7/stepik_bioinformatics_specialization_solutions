from .neighbors import find_neighbors_with_expected_hamming_distance


def find_most_frequent_k_mers_with_mismatches(text, k, expected_hamming_distance):

    length_of_text = len(text)

    map_to_store_the_frequency_of_words_with_mismatches = {}

    set_to_store_the_most_frequent_words_with_mismatches = set()

    for i in range(0, length_of_text - k + 1):

        pattern = text[i: i + k]

        neighborhood_set = find_neighbors_with_expected_hamming_distance(pattern, expected_hamming_distance)

        for neighbour in neighborhood_set:

            if neighbour not in map_to_store_the_frequency_of_words_with_mismatches.keys():
                map_to_store_the_frequency_of_words_with_mismatches[neighbour] = 1

            else:
                map_to_store_the_frequency_of_words_with_mismatches[neighbour] += 1

    max_frequency = -1

    for neighbour in map_to_store_the_frequency_of_words_with_mismatches.keys():
        if map_to_store_the_frequency_of_words_with_mismatches[neighbour] > max_frequency:
            max_frequency = map_to_store_the_frequency_of_words_with_mismatches[neighbour]

    for neighbour in map_to_store_the_frequency_of_words_with_mismatches.keys():
        if map_to_store_the_frequency_of_words_with_mismatches[neighbour] == max_frequency:
            set_to_store_the_most_frequent_words_with_mismatches.add(neighbour)

    return set_to_store_the_most_frequent_words_with_mismatches
