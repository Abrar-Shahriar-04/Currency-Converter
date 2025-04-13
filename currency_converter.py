exchange_rates = {
    "USD": 1.0,       # US Dollar
    "EUR": 0.92,      # Euro
    "GBP": 0.79,      # British Pound
    "JPY": 151.5,     # Japanese Yen
    "BDT": 109.0,     # Bangladeshi Taka
    "CNY": 7.23,      # Chinese Yuan
    "CAD": 1.37,      # Canadian Dollar
    "AUD": 1.53,      # Australian Dollar
    "RUB": 93.0,      # Russian Ruble
    "AED": 3.67       # UAE Dirham
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency code. Please try again.")
        return None
    if from_currency == to_currency:
        print(f"No conversion needed.")
        return amount
        
    # Convert to USD first
    amount_in_usd = amount / exchange_rates[from_currency]

    # Then from USD to target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]

    return converted_amount

def run_converter():
    print("\n====== Welcome to Currency Converter ======")
    print("Available currencies:")
    for currency in exchange_rates:
        print(f"- {currency}")     # Display available currencies

    from_curr = input("\nConvert from (currency code): ").strip().upper()
    to_curr = input("Convert to (currency code): ").strip().upper()

    try:
        amount = float(input("Amount to convert: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    result = convert_currency(amount, from_curr, to_curr)
    if result is not None:
        print(f"\n {amount} {from_curr} = {round(result, 2)} {to_curr}")

# Main loop
while True:
    run_converter()
    again = input("\nDo you want to convert again? (yes/no): ").strip().lower()
    if again != "yes":
        print("\nThank you for using the Currency Converter. Goodbye!")
        break
