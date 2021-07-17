import finding_hidden_messages_in_dna
import sys
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


def plot_occurrences(occurrence_indices):
    occurrence_indices = occurrence_indices[3:-10]
    for index in occurrence_indices:
        plt.axvline(x=index)
    plt.show()


def main():
    input_file = open("large_input.txt", "r")
    # pattern = input_file.readline().strip()
    text = input_file.readline().strip()

    pattern = "CTTGATCAT"
    # text = "GATATATGCATATACTT"

    occurrence_indices = finding_hidden_messages_in_dna.find_all_occurrences_of_pattern_in_text(text, pattern)

    sys.stdout = open("output.txt", "w")
    for index in occurrence_indices:
        print(index, end=" ")

    plot_occurrences(occurrence_indices)


if __name__ == "__main__":
    main()
