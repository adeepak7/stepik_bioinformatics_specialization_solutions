import finding_hidden_messages_in_dna

if __name__ == "__main__":

    input_file = open('/Users/adeepak7/Documents/MOOC/Coursera/Coursera-Bioinformatics-Specialization-Solutions/finding_hidden_messages_in_dna/datasets/salmonella_enterica.txt', 'r')
    text = ""

    while True:

        input_line = input_file.readline().strip()

        if input_line == '':
            break

        text += input_line

    map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value, set_of_most_frequent_k_mers_who_are_exactly_present_in_the_text = finding_hidden_messages_in_dna.find_dnaa_box_based_on_mismatches_and_reverse_complements(text, 9, 500, 1)

    for location in map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value.keys():

        print(location, map_to_store_the_most_frequent_k_mers_in_a_window_of_given_length_around_minimum_skew_value[location])

    print("K-mers: ")
    for k_mer in set_of_most_frequent_k_mers_who_are_exactly_present_in_the_text:

        print(k_mer, end=", ")
