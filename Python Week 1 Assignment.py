#Part 1: Input & Output Functions (print & input) 

#1. Print "Hello, World!" and your name on two separate lines
print("Hello, World!")
print("Anam Hunzah")

#2. Ask the user for their favorite color
color = input("Enter your favorite color: ")
print("Your favorite color is " + color)

#3. Display three different words separated by a hyphen
print("Python", "Programming", "Language", sep="-")

#4. Ask for birth year and print the age
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print("Your age is", age)

#5. Print the result of 5 + 5
print("The sum of 5 and 5 is", 5 + 5)

#6. Use the end parameter
print("Hello", end=" ")
print("World")

#7. Take two strings and join them 
first = input("Enter first string: ")
second = input("Enter second string: ")
print(first + " " + second) # use  " " for space between two strings

#8. Greeting in uppercase
name = input("Enter your name: ")
print(f"Welcome, {name}!".upper())

#9. Ask for city and country
city = input("Enter your city: ")
country = input("Enter your country: ")
print(f"{city}, {country}")

#10. Add a string and an integer using str()
age = 25
print("My age is " + str(age))
