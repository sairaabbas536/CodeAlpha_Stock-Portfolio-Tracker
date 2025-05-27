# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 300
}

# Ask user for stock names and quantities
portfolio = {}
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        qty = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = qty
    else:
        print("Stock not found in price list.")

# Calculate total investment
total = 0
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} x {stock_prices[stock]} = {value}")
    total += value

print(f"\nTotal Investment: ${total}")

# Optional: Save to file
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio.txt", "w") as file:
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} x {stock_prices[stock]} = {value}\n")
        file.write(f"\nTotal Investment: ${total}")
    print("Saved to portfolio.txt")