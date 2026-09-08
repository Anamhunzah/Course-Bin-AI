# Question 7: Distribute Items Equally - You have n candies and k students.
# Find how many candies each student gets and how many are left.

candies = int(input("Enter number of candies: "))
students = int(input("Enter number of students: "))

if students > 0:
    each_student = candies // students
    remaining = candies % students

    print("Each student gets:", each_student, "candies")
    print("Candies left:", remaining)

else:
    print("Number of students must be greater than 0.")