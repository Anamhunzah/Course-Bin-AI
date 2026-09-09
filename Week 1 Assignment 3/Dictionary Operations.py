# Dictionary Operations Assignment
# Check if a key exists in a dictionary.

data = {"name": "Ali", "age": 25, "city": "Lahore"}

key = input("Enter key to search: ")

if key in data:
    print("Key exists.")
else:
    print("Key does not exist.")

# Add a key-value pair to a dictionary.

data = {"name": "Ali", "age": 25}

key = input("Enter new key: ")
value = input("Enter value: ")

data[key] = value

print("Updated dictionary:", data)

# Find the sum of all the items in a dictionary.

data = {"a": 10, "b": 20, "c": 30}

total = 0

for value in data.values():
    total += value

print("Sum:", total)

# Multiply all the items in a dictionary.

data = {"a": 2, "b": 3, "c": 4}

product = 1

for value in data.values():
    product *= value

print("Product:", product)

# Create a dictionary containing numbers from 1 to n in the form (x, x*x).

n = int(input("Enter n: "))

data = {}

for x in range(1, n + 1):
    data[x] = x * x

print(data)

# Concatenate two dictionaries.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

combined = dict1.copy()
combined.update(dict2)

print("Combined dictionary:", combined)