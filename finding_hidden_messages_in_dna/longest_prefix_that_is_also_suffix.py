
def longest_prefix_that_is_also_suffix(pattern):

    length_of_pattern = len(pattern)
    lps = [0] * length_of_pattern

    temporary_len = 0
    i = 1

    while i < length_of_pattern:

        if pattern[temporary_len] == pattern[i]:
            temporary_len = temporary_len + 1
            lps[i] = temporary_len
            i = i + 1

        else:
            if temporary_len != 0:
                temporary_len = lps[temporary_len - 1]
            else:
                lps[i] = 0
                i = i + 1

    return lps
