from finding_hidden_messages_in_dna import find_all_most_frequent_k_mers


if __name__ == "__main__":

    input_file = open("input.txt", "r")
    text = input_file.readline().strip()
    k = int(input_file.readline().strip())

    # text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    # k = 4

    list_of_all_most_frequent_k_mers = find_all_most_frequent_k_mers(text, k)

    for k_mer in list_of_all_most_frequent_k_mers:
        print(k_mer, end=" ")
