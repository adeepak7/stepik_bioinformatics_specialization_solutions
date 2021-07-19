import sys
import finding_hidden_messages_in_dna


def main():
    input_file = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    text = input_file.readline().strip()
    K, expected_hamming_distance = map(int, input_file.readline().strip().split())

    set_to_store_the_most_frequent_words_with_mismatches = finding_hidden_messages_in_dna.find_most_frequent_k_mers_with_mismatches(
        text, K, expected_hamming_distance)

    for most_frequent_kmer in set_to_store_the_most_frequent_words_with_mismatches:
        print(most_frequent_kmer, end=" ")


if __name__ == "__main__":
    main()
