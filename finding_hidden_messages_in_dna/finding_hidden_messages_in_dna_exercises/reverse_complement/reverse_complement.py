from finding_hidden_messages_in_dna import find_reverse_complement


def main():

    input_file = open("input.txt", "r")
    text = input_file.readline().strip()

    print(find_reverse_complement(text))


if __name__ == "__main__":
    main()
