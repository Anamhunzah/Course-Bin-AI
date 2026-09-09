# String Manipulation 1:
# Create a new string made of an input string's first, middle, and last character.

text = input("Enter a string: ")

if len(text) >= 3:
    middle = len(text) // 2
    new_string = text[0] + text[middle] + text[-1]
    print("New string:", new_string)
else:
    print("Please enter at least 3 characters.")

# String Manipulation 2:
# Count occurrences of all characters within a given string.

text = input("Enter a string: ")
counts = {}

for char in text:
    counts[char] = counts.get(char, 0) + 1

print("Character occurrences:")
for char, count in counts.items():
    print(repr(char), ":", count)

# String Manipulation 3:
# Reverse a given string.

text = input("Enter a string: ")
print("Reversed string:", text[::-1])

# String Manipulation 4:
# Split a string on hyphens.

text = input("Enter a hyphen-separated string: ")
parts = text.split("-")

print("Split result:", parts)

# String Manipulation 5:
# Remove special symbols / punctuation from a string.

import string

text = input("Enter a string: ")
cleaned = ""

for char in text:
    if char not in string.punctuation:
        cleaned += char

print("String without punctuation:", cleaned)