from .kmp import kmp
import collections


def find_all_most_frequent_k_mers(text, k):
    """

    Parameters
    ----------
    text : string
        The DNA string
    k : string
        length of k-mer

    Returns
    -------
    python list
        list of all most frequent k-mers

    Notes
    ______
        C = constant
        Time Complexity: (Text - k + 1) * (k + Text + k + C) + 2 * O(Text - k + 1) = O( (Text - k) * (Text + k))

    """

    length_of_text = len(text)  # O(Text)

    hashmap_to_store_the_count_of_k_mer = collections.OrderedDict()

    for i in range(0, length_of_text - k + 1):  # O(Text - k + 1)

        k_mer = text[i:i + k]  # O(k)

        count_of_k_mer = kmp(text, k_mer)  # O(Text + k)

        hashmap_to_store_the_count_of_k_mer[k_mer] = count_of_k_mer  # O(C)

    maximum_count_of_any_k_mer = -1

    for k_mer in hashmap_to_store_the_count_of_k_mer:  # O(Text - k + 1)
        if hashmap_to_store_the_count_of_k_mer[k_mer] > maximum_count_of_any_k_mer:
            maximum_count_of_any_k_mer = hashmap_to_store_the_count_of_k_mer[k_mer]

    list_of_all_most_frequent_k_mer = []
    for k_mer in hashmap_to_store_the_count_of_k_mer:  # O(Text - k + 1)
        if hashmap_to_store_the_count_of_k_mer[k_mer] == maximum_count_of_any_k_mer:
            list_of_all_most_frequent_k_mer.append(k_mer)

    return list_of_all_most_frequent_k_mer
