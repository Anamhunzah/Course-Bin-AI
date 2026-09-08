#Question 3: Calculate Compound Interest. Use the formula: CI = P * (1 + R/100)**T - P 
#Where P = principal, R = rate, T = time 

P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time in years: "))

CI = P * (1 + R/100)**T - P

print("Compound Interest:", CI)