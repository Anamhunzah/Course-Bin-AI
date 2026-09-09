# AI-ML Course - Week 1 - Assignment 3
# String Manipulation:
# Check if a String is a Pangram or Not.

text = input("Enter a sentence: ").lower()

letters = set()

for char in text:
    if 'a' <= char <= 'z':
        letters.add(char)

if len(letters) == 26:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")

# Replace every blank space with a hyphen in a string.

text = input("Enter a string: ")
result = text.replace(" ", "-")

print("Result:", result)

# Display letters that are in the two strings but not in both.

first = input("Enter first string: ").lower()
second = input("Enter second string: ").lower()

letters1 = set(first)
letters2 = set(second)

result = letters1.symmetric_difference(letters2)

print("Letters in one string but not both:", result)

# Find the larger string without using built-in length functions.

first = input("Enter first string: ")
second = input("Enter second string: ")

count1 = 0
for char in first:
    count1 += 1

count2 = 0
for char in second:
    count2 += 1

if count1 > count2:
    print("Larger string:", first)
elif count2 > count1:
    print("Larger string:", second)
else:
    print("Both strings have the same length.")

# Count uppercase and lowercase letters in a string.

text = input("Enter a string: ")

uppercase = 0
lowercase = 0

for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)

# Check if two strings are anagrams.

first = input("Enter first string: ").replace(" ", "").lower()
second = input("Enter second string: ").replace(" ", "").lower()

if sorted(first) == sorted(second):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# Check if a substring is present in the given string.

text = input("Enter the main string: ")
substring = input("Enter the substring: ")

if substring in text:
    print("Substring is present.")
else:
    print("Substring is not present.")

# Print all permutations of a string in lexicographic order without recursion.

from itertools import permutations

text = input("Enter a string: ")

permutation_set = set(permutations(text))
sorted_permutations = sorted(permutation_set)

for item in sorted_permutations:
    print("".join(item))

# Calculate the length of a string without using library functions.

text = input("Enter a string: ")

length = 0

for char in text:
    length += 1

print("Length:", length)

# Create a new string made of the first 2 and last 2 characters.

text = input("Enter a string: ")

if len(text) >= 2:
    new_string = text[:2] + text[-2:]
    print("New string:", new_string)
else:
    print("Please enter at least 2 characters.")
    