# Dictionary Manipulation 1:
# Check if a value exists in a dictionary.

data = {"name": "Ali", "age": 25, "city": "Lahore"}

value = input("Enter a value to search for: ")

if value in [str(v) for v in data.values()]:
    print("Value exists in the dictionary.")
else:
    print("Value does not exist in the dictionary.")

# Dictionary Manipulation 2:
# Get the key of a minimum value from the following dictionary.

data = {"Ali": 75, "Sara": 62, "Ahmed": 88, "Zara": 55}

minimum_key = min(data, key=data.get)

print("Dictionary:", data)
print("Key with minimum value:", minimum_key)
print("Minimum value:", data[minimum_key])

# Dictionary Manipulation 3:
# Delete a list of keys from a dictionary.

data = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore",
    "country": "Pakistan",
    "course": "AI-ML"
}

keys_to_delete = ["age", "country"]

for key in keys_to_delete:
    data.pop(key, None)

print("Updated dictionary:", data)