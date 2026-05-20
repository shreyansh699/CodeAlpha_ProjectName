stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:
    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Added {stock_name} worth ${investment}")

    else:
        print("Stock not available.")

print("\nTotal Investment Value: $", total_investment)

file = open("portfolio.txt", "w")
file.write(f"Total Investment: ${total_investment}")
file.close()

print("Portfolio saved to portfolio.txt")
