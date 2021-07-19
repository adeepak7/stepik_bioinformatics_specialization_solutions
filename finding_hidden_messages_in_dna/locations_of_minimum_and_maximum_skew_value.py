import math


def find_locations_of_minimum_and_maximum_skew_value(text):

    length_of_text = len(text)

    locations_for_minimum_skew_value = []
    locations_for_maximum_skew_value = []

    minimum_skew_value = math.inf
    maximum_skew_value = -1 * math.inf
    skew_value = 0

    for i in range(0, length_of_text):

        if text[i] == 'G':
            skew_value += 1
        elif text[i] == 'C':
            skew_value -= 1

        if skew_value < minimum_skew_value:
            minimum_skew_value = skew_value
            locations_for_minimum_skew_value.clear()
            locations_for_minimum_skew_value.append(i)

        elif skew_value == minimum_skew_value:
            locations_for_minimum_skew_value.append(i)

        if skew_value > maximum_skew_value:
            maximum_skew_value = skew_value
            locations_for_maximum_skew_value.clear()
            locations_for_maximum_skew_value.append(i)

        elif skew_value == maximum_skew_value:
            locations_for_maximum_skew_value.append(i)

    return minimum_skew_value, maximum_skew_value, locations_for_minimum_skew_value, locations_for_maximum_skew_value
