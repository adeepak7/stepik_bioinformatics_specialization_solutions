import sys
import finding_hidden_messages_in_dna


def main():
    input_file = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    text1 = input_file.readline().strip()
    text2 = input_file.readline().strip()

    hamming_distance = finding_hidden_messages_in_dna.find_hamming_distance(text1, text2)

    print(hamming_distance)


if __name__ == "__main__":
    main()
