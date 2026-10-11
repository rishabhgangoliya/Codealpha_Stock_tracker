"""Task 2: Stock Portfolio Tracker

Calculates total investment value from user-entered stock names and quantities,
using a hardcoded dictionary of stock prices. Optionally saves the result to a file.
"""

# Hardcoded stock prices (price per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def get_portfolio():
    """Ask the user for stock names and quantities. Returns {stock: quantity}."""
    portfolio = {}
    print("Available stocks:", ", ".join(f"{s} (${p})" for s, p in STOCK_PRICES.items()))
    print("Enter stock names and quantities. Type 'done' when finished.\n")

    while True:
        name = input("Stock name (or 'done'): ").strip().upper()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print(f"  '{name}' is not in the price list. Try again.")
            continue

        qty_text = input(f"Quantity of {name}: ").strip()
        try:
            qty = int(qty_text)
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if qty <= 0:
            print("  Quantity must be greater than zero.")
            continue

        # If the same stock is entered twice, add to the existing quantity
        portfolio[name] = portfolio.get(name, 0) + qty

    return portfolio


def calculate_total(portfolio):
    """Returns (list of (stock, qty, price, value), total_investment)."""
    rows = []
    total = 0
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = qty * price
        rows.append((stock, qty, price, value))
        total += value
    return rows, total


def display(rows, total):
    print("\n" + "=" * 45)
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>14}")
    print("-" * 45)
    for stock, qty, price, value in rows:
        print(f"{stock:<8}{qty:>6}{price:>10}{value:>14}")
    print("-" * 45)
    print(f"{'Total investment:':<24}{total:>21}")
    print("=" * 45)


def save_to_file(rows, total):
    choice = input("\nSave result to a file? (txt/csv/no): ").strip().lower()
    if choice == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio\n")
            for stock, qty, price, value in rows:
                f.write(f"{stock}: {qty} x {price} = {value}\n")
            f.write(f"Total investment: {total}\n")
        print("Saved to portfolio.txt")
    elif choice == "csv":
        with open("portfolio.csv", "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty, price, value in rows:
                f.write(f"{stock},{qty},{price},{value}\n")
            f.write(f"Total,,,{total}\n")
        print("Saved to portfolio.csv")
    else:
        print("Not saved.")


def main():
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered.")
        return
    rows, total = calculate_total(portfolio)
    display(rows, total)
    save_to_file(rows, total)


if __name__ == "__main__":
    main()