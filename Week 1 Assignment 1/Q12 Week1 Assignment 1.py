# Question 12: Currency Converter (USD to PKR)
# Input amount in USD and convert using a fixed exchange rate.

usd_amount = float(input("Enter amount in USD: "))
exchange_rate = 285  # Suppose exchange rate
pkr_amount = usd_amount * exchange_rate

print("Amount in USD:", usd_amount)
print("Amount in PKR:", pkr_amount)