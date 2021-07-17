
def find_reverse_complement(text):

    length_of_text = len(text)

    reverse_complement_of_text = ""

    complementary_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}

    for i in range(length_of_text - 1, -1, -1):
        reverse_complement_of_text += complementary_bases[text[i]]

    return reverse_complement_of_text
