import finding_hidden_messages_in_dna
import sys


def main():
    input_file = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    pattern = input_file.readline().strip()
    text = input_file.readline().strip()
    expected_hamming_distance = int(input_file.readline().strip())

    approximate_occurrences_list = finding_hidden_messages_in_dna.find_all_approximate_occurrences_of_pattern_with_given_hamming_distance_in_text(
        text, pattern, expected_hamming_distance)

    print("Count:", len(approximate_occurrences_list))

    for index in approximate_occurrences_list:
        print(index, end=" ")


if __name__ == "__main__":
    main()
