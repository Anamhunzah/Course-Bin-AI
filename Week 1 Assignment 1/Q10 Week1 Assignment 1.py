# Question 10: Salary Calculator - Input basic salary.
# HRA = 20% of basic, DA = 15% of basic, Total Salary = Basic + HRA + DA

basic_salary = float(input("Enter basic salary: "))

HRA = 0.20 * basic_salary
DA = 0.15 * basic_salary

total_salary = basic_salary + HRA + DA

print("Total Salary:", total_salary)
print("HRA:", HRA)
print("DA:", DA)
print("Total Salary:", total_salary)