
def generate_frequency_table(text, k):

    length_of_text = len(text)

    frequency_of_each_k_mer = {}

    for i in range(0, length_of_text - k + 1):

        k_mer = text[i: i + k]

        if k_mer not in frequency_of_each_k_mer:
            frequency_of_each_k_mer[k_mer] = 1
        else:
            frequency_of_each_k_mer[k_mer] = frequency_of_each_k_mer[k_mer] + 1

    return frequency_of_each_k_mer
