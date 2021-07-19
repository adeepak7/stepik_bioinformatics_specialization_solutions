"""
Time Complexity: O(Text + Pattern)
"""


from finding_hidden_messages_in_dna import kmp

input_file = open("input.txt", "r")

text = input_file.readline().strip()

pattern = input_file.readline().strip()

print(text)
print(pattern)

print(kmp(text, pattern))
