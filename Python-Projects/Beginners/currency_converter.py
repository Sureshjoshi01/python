# Currency Converter
# Write a program to convert an amount of money from one currency to another
# using fixed exchange rates. The user inputs the amount and selects the currencies
# for conversion.
# Optional Enhancements
# • Modify the program so that the user can see the equivalent amount in several
# different currencies at the same time. For example, converting 100 USD to
# EUR, CAD, and GBP all at once.
# • Expand the list of available currencies for conversion. This might involve
# adding more fixed exchange rates to the program.
# • Keep a history of the most recent conversions made during the session and
# display this history at the end of the program.

import csv

def exchange_rates():
    try:
        rates = {}
        with open("exchange_rates.csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 2:
                    print(f"Invalid row found: {row}")
                    continue
                currency = row[0].strip().upper()
                try:
                    rate = float(row[1])
                except ValueError:
                    print(f"Invalid rate for {currency}")
                    continue
                rates[currency] = rate
        return rates
    except FileNotFoundError:
        print("Error Loading the Program, exchange rate file does not exists")
        return None
        
    
def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))

            if amount <= 0:
                print("Amount must be greater than zero")
                continue
            return amount
        except ValueError:
            print("You need to enter only numbers")

def get_currency(prompt, exchange_rate):
    currencies = exchange_rate.keys()
    while True:
        print(f"\nAvailable currencies: {', '.join(currencies)}")
        currency = input(prompt).upper()
        if currency in currencies:
            return currency
        print(f"{currency} currency is not available")

def convert_currency(amount, src_currency, trgt_currency, exchange_rate):
    if src_currency == trgt_currency:
        return amount
    source_rate = exchange_rate[src_currency]
    target_rate = exchange_rate[trgt_currency]
    return (amount / source_rate) * target_rate

def currency_convertor():
    exchange_rate = exchange_rates()
    if exchange_rate is None:
        return
    history = []
    while True:
        amount = get_amount()
        src_currency = get_currency(
            "Source currency: ",
            exchange_rate
        )

        trgt_currency = get_currency(
            "Target currency: ",
            exchange_rate
        )

        result = convert_currency(
            amount,
            src_currency,
            trgt_currency,
            exchange_rate
        )

        print(
            f"\n{amount} {src_currency} = "
            f"{result:.2f} {trgt_currency}"
        )

        history.append(
            f"{amount} {src_currency} -> "
            f"{result:.2f} {trgt_currency}"
        )

        choice = input(
            "\nDo another conversion? (Y/N): "
        ).upper()

        if choice != "Y":
            break

currency_convertor()