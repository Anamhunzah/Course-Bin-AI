# Question 11: Age in Months and Days - Input age in years. Calculate and print age in months and approximate days.

age_years = int(input("Enter age in years: "))
age_months = age_years * 12
age_days = age_years * 365

print("Age in months:", age_months)
print("Age in approximate days:", age_days)