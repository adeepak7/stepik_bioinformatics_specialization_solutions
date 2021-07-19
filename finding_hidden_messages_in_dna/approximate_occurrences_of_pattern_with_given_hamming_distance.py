from .hamming_distance import find_hamming_distance


def find_all_approximate_occurrences_of_pattern_with_given_hamming_distance_in_text(text, pattern,
                                                                                    expected_hamming_distance):
    length_of_text = len(text)
    length_of_pattern = len(pattern)

    approximate_occurrences_list = []

    for i in range(0, length_of_text):

        temp_text = text[i: i + length_of_pattern]

        if find_hamming_distance(temp_text, pattern) <= expected_hamming_distance:
            approximate_occurrences_list.append(i)

    return approximate_occurrences_list
