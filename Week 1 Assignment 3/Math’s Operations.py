# Math Operations Assignment
# Find the area of a triangle using three sides (Heron's formula).

import math

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of triangle:", area)
else:
    print("These sides do not form a valid triangle.")

# Find quotient and remainder of two numbers.

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

if divisor != 0:
    quotient = dividend // divisor
    remainder = dividend % divisor

    print("Quotient:", quotient)
    print("Remainder:", remainder)
else:
    print("Divisor cannot be zero.")

# Print an identity matrix of size n.

n = int(input("Enter matrix size: "))

for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

# Find the LCM of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = abs(a)
y = abs(b)

if x == 0 or y == 0:
    print("LCM:", 0)
else:
    multiple = max(x, y)

    while multiple % x != 0 or multiple % y != 0:
        multiple += 1

    print("LCM:", multiple)

# Find the sum of first N natural numbers.

n = int(input("Enter number of terms: "))

if n >= 0:
    total = n * (n + 1) // 2
    print("Sum:", total)
else:
    print("Enter a non-negative number.")

# Check if two numbers are amicable numbers.

def proper_divisor_sum(number):
    if number <= 1:
        return 0

    total = 1

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            total += divisor
            other = number // divisor
            if other != divisor:
                total += other

    return total

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a != b and proper_divisor_sum(a) == b and proper_divisor_sum(b) == a:
    print("They are amicable numbers.")
else:
    print("They are not amicable numbers.")

# Find all perfect squares in a range where the sum of digits is less than 10.

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

if start > end:
    start, end = end, start

squares = []

n = 1
while n * n <= end:
    square = n * n

    if square >= start:
        digit_sum = sum(int(digit) for digit in str(square))

        if digit_sum < 10:
            squares.append(square)

    n += 1

print("Perfect squares:", squares)

# Check whether a number is an Armstrong number.

number = int(input("Enter a number: "))

if number < 0:
    print("Negative numbers are not considered Armstrong numbers here.")
else:
    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    if total == number:
        print("It is an Armstrong number.")
    else:
        print("It is not an Armstrong number.")