"""
finding_hidden_messages_in_dna
-------------------------------
-------------------------------

A package that encapsulates the solutions to the Coursera Bioinformatics specialization.
"""

__author__ = "Deepak Tatyaji Ahire"
__version__ = '0.1.0'

from .longest_prefix_that_is_also_suffix import longest_prefix_that_is_also_suffix
from .kmp import kmp
from .reverse_complement import find_reverse_complement
from .kmp_find_all_Occurrences import find_all_occurrences_of_pattern_in_text
from .frequency_table import generate_frequency_table
from .skew_value import find_skew_value
from .locations_of_minimum_and_maximum_skew_value import find_locations_of_minimum_and_maximum_skew_value
from .hamming_distance import find_hamming_distance
from .approximate_occurrences_of_pattern_with_given_hamming_distance import find_all_approximate_occurrences_of_pattern_with_given_hamming_distance_in_text
from .neighbors import find_neighbors_with_expected_hamming_distance
from .most_frequent_k_mers_with_mismatches import find_most_frequent_k_mers_with_mismatches
from .most_frequent_k_mers_and_respective_reverse_complements_with_mismatches import find_most_frequent_k_mers_and_respective_reverse_complements_with_mismatches
from .most_frequent_k_mers_in_text import find_all_most_frequent_k_mers
from .clumps_in_text import find_clumps_in_text
from .dnaa_box_based_on_mismatches_and_reverse_complements import find_dnaa_box_based_on_mismatches_and_reverse_complements
