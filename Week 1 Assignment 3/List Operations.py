# List Operations Assignment
# Find the largest number in a list.

numbers = [12, 45, 7, 89, 34, 23]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("List:", numbers)
print("Largest number:", largest)

# Find the second largest number in a list.

numbers = [12, 45, 7, 89, 34, 23]

unique_numbers = list(set(numbers))

if len(unique_numbers) >= 2:
    unique_numbers.sort()
    print("Second largest number:", unique_numbers[-2])
else:
    print("At least two different numbers are required.")

# Print the largest even and largest odd number in a list.

numbers = [12, 45, 7, 89, 34, 23, 100, 18]

even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]

if even_numbers:
    print("Largest even number:", max(even_numbers))
else:
    print("No even number found.")

if odd_numbers:
    print("Largest odd number:", max(odd_numbers))
else:
    print("No odd number found.")

# Find the average of a list.

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

if len(numbers) > 0:
    average = total / len(numbers)
    print("Average:", average)
else:
    print("List is empty.")

# Count occurrences of an element in a list.

numbers = [1, 2, 3, 2, 4, 2, 5, 2]

target = int(input("Enter number to search: "))

count = 0

for number in numbers:
    if number == target:
        count += 1

print("Occurrences:", count)

# Remove duplicates from a list.

numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original list:", numbers)
print("Without duplicates:", unique_numbers)

# Find the number occurring an odd number of times in a list.

numbers = [2, 3, 2, 4, 4, 3, 5, 5, 5]

for number in set(numbers):
    if numbers.count(number) % 2 != 0:
        print("Number occurring odd number of times:", number)

# Find the union of two lists.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

union = list(set(list1) | set(list2))

print("Union:", union)

# Swap the first and last element in a list.

numbers = [10, 20, 30, 40, 50]

if len(numbers) >= 2:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("Updated list:", numbers)

# Return the word with the longest length from a list of words.

words = ["Python", "AI", "Machine", "Learning", "Programming"]

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
print("Length:", len(longest_word))

# Generate random numbers from 1 to 20 and append them to a list.

import random

n = int(input("How many random numbers do you want? "))

numbers = []

for _ in range(n):
    numbers.append(random.randint(1, 20))

print("Generated list:", numbers)