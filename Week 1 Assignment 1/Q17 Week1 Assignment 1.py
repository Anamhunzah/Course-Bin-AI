# Question 17:Convert Minutes to Hours and Minutes. Input number of minutes and convert to hours and remaining minutes.
# Example: 130 minutes = 2 hours 10 minutes

minutes = int(input("Enter number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours:", hours)
print("Remaining Minutes:", remaining_minutes)