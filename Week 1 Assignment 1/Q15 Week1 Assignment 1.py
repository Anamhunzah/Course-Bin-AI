# Question 15: Speed, Distance, and Time. Input distance and time and calculate speed.
# Formula: Speed = Distance / Time

distance = float(input("Enter distance: "))
time = float(input("Enter time: "))

if time > 0:
    speed = distance / time
    print("Speed:", speed)

else:
    print("Time must be greater than 0.")