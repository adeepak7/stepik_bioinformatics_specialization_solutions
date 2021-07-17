
def find_skew_value(text):

    length_of_text = len(text)

    skew_value = 0
    skew_value_list = []

    for i in range(0, length_of_text):

        if text[i] == 'C':
            skew_value = skew_value - 1
        elif text[i] == 'G':
            skew_value = skew_value + 1

        skew_value_list.append(skew_value)

    return text, skew_value_list
