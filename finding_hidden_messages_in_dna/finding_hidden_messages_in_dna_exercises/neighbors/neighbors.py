import sys
from finding_hidden_messages_in_dna import find_neighbors_with_expected_hamming_distance


def main():
    input_file = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    pattern = input_file.readline().strip()
    expected_hamming_distance = int(input_file.readline().strip())

    neighborhood_set = find_neighbors_with_expected_hamming_distance(pattern, expected_hamming_distance)

    for neighbor in neighborhood_set:
        print(neighbor)


if __name__ == "__main__":
    main()
