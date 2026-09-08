#Question 8: Calculate Profit or Loss Input cost price and selling price.
# Display Profit and amount, Loss and amount, or No Profit No Loss.

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:

    profit = selling_price - cost_price
    print("Profit:", profit)

elif selling_price < cost_price:

    loss = cost_price - selling_price
    print("Loss:", loss)

else:
    print("No Profit No Loss.")