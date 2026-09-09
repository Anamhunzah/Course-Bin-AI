# Loop Manipulation 1:
# Print first 10 natural numbers using while.

number = 1

while number <= 10:
    print(number)
    number += 1

# Loop Manipulation 2:
# Take input from user and print even numbers till that input number.

n = int(input("Enter the limit: "))

number = 2

while number <= n:
    print(number, end=" ")
    number += 2

print()

# Loop Manipulation 3:
# Take input from user and print odd numbers till that input number.

n = int(input("Enter the limit: "))

number = 1

while number <= n:
    print(number, end=" ")
    number += 2

print()

# Loop Manipulation 4:
# Take input from user and print prime numbers till that input number.

n = int(input("Enter the limit: "))

for number in range(2, n + 1):
    is_prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")

print()

# Loop Manipulation 5:
# Print multiplication table of a given number.

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)