# List Manipulation 1:
# Reverse a list in Python.

numbers = [10, 20, 30, 40, 50]
numbers.reverse()

print("Reversed list:", numbers)

# List Manipulation 2:
# Turn every item of a list into its square.

numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]

print("Original list:", numbers)
print("Squared list:", squares)

# List Manipulation 3:
# Remove empty strings from the list of strings.

words = ["Python", "", "AI", "", "Machine Learning", "", "Data"]

words = [word for word in words if word != ""]

print("List after removing empty strings:", words)

# List Manipulation 4:
# Add a new item to a list after a specified item.

items = ["apple", "banana", "orange", "mango"]

specified_item = input("Enter the item after which to add: ")
new_item = input("Enter the new item: ")

if specified_item in items:
    index = items.index(specified_item)
    items.insert(index + 1, new_item)
    print("Updated list:", items)
else:
    print("Specified item was not found.")

# List Manipulation 5:
# Replace a list item with a new value if found.

items = ["apple", "banana", "orange", "mango"]

old_value = input("Enter item to replace: ")
new_value = input("Enter new value: ")

if old_value in items:
    index = items.index(old_value)
    items[index] = new_value
    print("Updated list:", items)
else:
    print("Item not found.")

print("Final list:", items)