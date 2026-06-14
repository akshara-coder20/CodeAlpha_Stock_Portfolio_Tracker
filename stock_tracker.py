# Stock Portfolio Tracker
stock_prices = {
    "AAPL": 180,
    "TSLA": 250
}

print("===== Stock Portfolio Tracker =====")

stock_name = input("Enter stock name (AAPL/TSLA): ").strip().upper()

try:
    quantity = int(input("Enter quantity: ").strip())
    if quantity < 0:
        raise ValueError
except ValueError:
    print("Please enter a valid non-negative integer for quantity.")
    exit(1)

if stock_name in stock_prices:
    total_value = stock_prices[stock_name] * quantity

    print("\n----- Portfolio Details -----")
    print("Stock Name:", stock_name)
    print("Price per Share: $", stock_prices[stock_name])
    print("Quantity:", quantity)
    print("Total Investment Value: $", total_value)
else:
    print("Stock not found!")