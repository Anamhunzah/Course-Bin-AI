#Question 9: Total Marks and Percentage Input marks of 5 subjects.
# Print Total Marks, Percentage, and Average.

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
marks4 = float(input("Enter marks for subject 4: "))
marks5 = float(input("Enter marks for subject 5: "))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total_marks / 500) * 100
average = total_marks / 5

print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Average:", average)