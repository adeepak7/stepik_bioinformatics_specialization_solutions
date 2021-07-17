import sys
from finding_hidden_messages_in_dna import find_skew_value


def main():

    input_file = open('input.txt', 'r')

    text = input_file.readline().strip()

    skew_value, skew_value_list = find_skew_value(text)

    sys.stdout = open('output.txt', 'w')

    print(len(skew_value_list))

    print(0, end=" ")

    for skew in skew_value_list:
        print(skew, end=" ")


if __name__ == "__main__":
    main()

