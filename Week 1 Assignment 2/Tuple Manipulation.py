# Tuple Manipulation 1:
# Reverse the tuple.

numbers = (10, 20, 30, 40, 50)

reversed_tuple = numbers[::-1]

print("Original tuple:", numbers)
print("Reversed tuple:", reversed_tuple)

# Tuple Manipulation 2:
# Access value 20 from the tuple.

numbers = (10, 20, 30, 40, 50)

print("Value 20:", numbers[1])

# Tuple Manipulation 3:
# Swap two tuples in Python.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("Before swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

tuple1, tuple2 = tuple2, tuple1

print("After swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)