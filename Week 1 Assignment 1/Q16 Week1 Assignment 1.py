# Question 16: BMI Calculator - Input weight (kg) and height (m). Calculate BMI and categorize it.
# BMI = weight / (height ** 2)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

if height > 0:
    BMI = weight / (height ** 2)
    print("Your BMI is:", BMI)

    if BMI < 18.5:
        print("Category: Underweight")
    elif BMI < 25:
        print("Category: Normal")
    elif BMI < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
        
else:
    print("Height must be greater than 0.")