"""
Module to compute the count of all the occurrences of the given pattern in the given text.
"""

from .longest_prefix_that_is_also_suffix import longest_prefix_that_is_also_suffix


def kmp(text, pattern):
    """
    Computes the count of all the occurrences of the given pattern in the given text.

    Parameters
    ----------
    text :
        The text string
    pattern :
        The pattern string

    Returns
    -------
    int
        count of all occurrences of pattern in the text

    """

    length_of_text = len(text)
    length_of_pattern = len(pattern)

    count_of_all_occurrences_of_pattern = 0

    lps = longest_prefix_that_is_also_suffix(pattern)

    i = 0
    j = 0

    while i < length_of_text:

        if text[i] == pattern[j]:
            i = i + 1
            j = j + 1

        if j == length_of_pattern:
            j = lps[j - 1]
            count_of_all_occurrences_of_pattern += 1

        elif i < length_of_text and text[i] != pattern[j]:

            if j != 0:
                j = lps[j - 1]
            else:
                i = i + 1

    return count_of_all_occurrences_of_pattern
