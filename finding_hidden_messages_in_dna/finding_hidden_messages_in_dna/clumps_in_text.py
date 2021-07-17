from .frequency_table import generate_frequency_table


def find_clumps_in_text(text, k, length_of_text_window, number_of_k_mers_expected):

    length_of_text = len(text)

    k_mers_with_clumps = set()

    for i in range(0, length_of_text - length_of_text_window + 1):

        text_window = text[i: i + length_of_text_window]

        frequency_of_each_k_mer = generate_frequency_table(text_window, k)

        for k_mer in frequency_of_each_k_mer.keys():

            if frequency_of_each_k_mer[k_mer] >= number_of_k_mers_expected:
                k_mers_with_clumps.add(k_mer)

    return k_mers_with_clumps
