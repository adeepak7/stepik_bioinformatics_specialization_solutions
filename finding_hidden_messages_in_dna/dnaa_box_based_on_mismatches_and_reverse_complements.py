from .locations_of_minimum_and_maximum_skew_value import find_locations_of_minimum_and_maximum_skew_value
from .most_frequent_k_mers_and_respective_reverse_complements_with_mismatches import \
    find_most_frequent_k_mers_and_respective_reverse_complements_with_mismatches
from .kmp import kmp


def find_dnaa_box_based_on_mismatches_and_reverse_complements(text, k, length_of_text_window,
                                                              expected_hamming_distance):

    list_of_locations_with_minimum_skew_value = find_locations_of_minimum_and_maximum_skew_value(text)[2]

    # Checking in the window of given size if we find any frequent k-mers and their reverse complements
    # with the given expected hamming distance

    map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value = {}

    for location in list_of_locations_with_minimum_skew_value:

        # window starting behind the location
        window_start = location - length_of_text_window + 1
        window_end = location + 1
        text_window = text[window_start: window_end]

        set_of_most_frequent_k_mers = find_most_frequent_k_mers_and_respective_reverse_complements_with_mismatches(
            text_window, k,
            expected_hamming_distance)

        if (location, window_start, window_end) not in map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value.keys():
            map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value[(location, window_start, window_end)] = set()

        for k_mer in set_of_most_frequent_k_mers:
            map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value[
                (location, window_start, window_end)].add(k_mer)

        # window starting from location

        window_start = location
        window_end = location + length_of_text_window
        text_window = text[window_start: window_end]

        set_of_most_frequent_k_mers = find_most_frequent_k_mers_and_respective_reverse_complements_with_mismatches(
            text_window, k,
            expected_hamming_distance)

        if (location, window_start, window_end) not in map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value.keys():
            map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value[
                (location, window_start, window_end)] = set()

        for k_mer in set_of_most_frequent_k_mers:
            map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value[
                (location, window_start, window_end)].add(k_mer)

    # Now filtering those 9-mers who are actually present in the text

    set_of_most_frequent_k_mers_who_are_exactly_present_in_the_text = set()

    for (location, window_start, window_end) in map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value.keys():
        for k_mer in map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value[(location, window_start, window_end)]:

            # Define the text window to check if k_mer is present in that window
            if kmp(text[window_start: window_end], k_mer) > 0:
                set_of_most_frequent_k_mers_who_are_exactly_present_in_the_text.add(k_mer)

    return map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value, set_of_most_frequent_k_mers_who_are_exactly_present_in_the_text
