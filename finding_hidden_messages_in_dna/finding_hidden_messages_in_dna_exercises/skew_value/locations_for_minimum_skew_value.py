import sys
from finding_hidden_messages_in_dna import find_locations_of_minimum_and_maximum_skew_value


def main():

    input_file = open('input.txt', 'r')

    text = input_file.readline().strip()

    minimum_skew_value, maximum_skew_value, locations_for_minimum_skew_value, locations_for_maximum_skew_value = find_locations_of_minimum_and_maximum_skew_value(text)

    sys.stdout = open('output.txt', 'w')

    for location in locations_for_maximum_skew_value:
        print(location, end=" ")


if __name__ == "__main__":
    main()
