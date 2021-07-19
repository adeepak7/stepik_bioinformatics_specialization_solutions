from finding_hidden_messages_in_dna import find_clumps_in_text


def main():

    input_file = open('large_input.txt', 'r')

    # sys.stdout = open('output.txt', 'w')

    text = input_file.readline().strip()

    # k, length_of_text_window, number_of_kmers_expected = map(int, input_file.readline().strip().split())

    print("Length of text: ", len(text))

    k, length_of_text_window, number_of_kmers_expected = "9 500 3".split()

    k = int(k.strip())
    length_of_text_window = int(length_of_text_window.strip())
    number_of_kmers_expected = int(number_of_kmers_expected.strip())

    print("k: ", k, "Length of text window: ", length_of_text_window, "Number of kmers expected: ", number_of_kmers_expected)

    k_mers_with_clumps = find_clumps_in_text(text, k, length_of_text_window, number_of_kmers_expected)

    for k_mer in k_mers_with_clumps:
        print(k_mer, end=" ")

    print("")

    print("Count of 9-mers:", len(k_mers_with_clumps))


if __name__ == "__main__":
    main()
