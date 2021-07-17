
def find_hamming_distance(text1, text2):

    length_of_text1 = len(text1)
    length_of_text2 = len(text2)

    difference_in_length = max(length_of_text1, length_of_text2) - min(length_of_text2, length_of_text1)

    hamming_distance = 0
    hamming_distance += difference_in_length

    for i in range(0, min(length_of_text1, length_of_text2)):

        if text1[i] != text2[i]:
            hamming_distance += 1

    return hamming_distance
