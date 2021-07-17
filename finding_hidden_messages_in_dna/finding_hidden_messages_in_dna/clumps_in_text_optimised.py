
def find_clumps_in_text(text, k, length_of_text_window, number_of_k_mers_expected):

    length_of_text = len(text)

    k_mers_with_clumps = set()

    occurrence_indices_of_k_mer = {}

    for i in range(0, length_of_text - k + 1):

        pattern = text[i: i + k]

        if pattern not in occurrence_indices_of_k_mer.keys():
            occurrence_indices_of_k_mer[pattern] = []
            occurrence_indices_of_k_mer[pattern].append(i)

        else:
            occurrence_indices_of_k_mer[pattern].append(i)

    for k_mer in occurrence_indices_of_k_mer.keys():

        occurrence_list_of_k_mer = occurrence_indices_of_k_mer[k_mer]
        length_of_occurrence_list_of_k_mer = len(occurrence_list_of_k_mer)

        verdict = False

        if length_of_occurrence_list_of_k_mer >= number_of_k_mers_expected:

            for i in range(0, length_of_occurrence_list_of_k_mer - number_of_k_mers_expected + 1):

                if occurrence_list_of_k_mer[i + number_of_k_mers_expected - 1] + k - 1 <= occurrence_list_of_k_mer[i] + length_of_text_window - 1:
                    verdict = True
                    print(occurrence_list_of_k_mer)
                    break

        if verdict:
            k_mers_with_clumps.add(k_mer)

    return k_mers_with_clumps
