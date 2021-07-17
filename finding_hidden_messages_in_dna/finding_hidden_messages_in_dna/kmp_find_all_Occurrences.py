from .longest_prefix_that_is_also_suffix import longest_prefix_that_is_also_suffix


def find_all_occurrences_of_pattern_in_text(text, pattern):

    length_of_text = len(text)
    length_of_pattern = len(pattern)

    lps = longest_prefix_that_is_also_suffix(pattern)

    i = 0
    j = 0

    occurrence_indices = []

    while i < length_of_text:

        if text[i] == pattern[j]:
            i = i + 1
            j = j + 1

        if j == length_of_pattern:
            occurrence_indices.append(i - j)
            j = lps[j - 1]

        elif (i < length_of_text) and (text[i] != pattern[j]):

            if j != 0:
                j = lps[j - 1]
            else:
                i = i + 1

    return occurrence_indices
