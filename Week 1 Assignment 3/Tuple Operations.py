# Tuple Operations Assignment
# Create a list of tuples with first element as number and second as square.

start = int(input("Enter start: "))
end = int(input("Enter end: "))

result = []

for number in range(start, end + 1):
    result.append((number, number ** 2))

print(result)

# Remove all tuples in a list of tuples outside the given roll-number range.
# Example uses USN prefixes with roll numbers.

prefix = input("Enter USN prefix (example: ABC): ")
lower = int(input("Enter lower roll number: "))
upper = int(input("Enter upper roll number: "))

students = [(prefix, roll) for roll in range(1, 21)]

filtered = [
    (usn_prefix, roll)
    for usn_prefix, roll in students
    if lower <= roll <= upper
]

print("Tuples within the range:")
print(filtered)