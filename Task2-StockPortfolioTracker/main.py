#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Professional Stock Portfolio Tracker
"""

import csv
import sys

# Check if yfinance is available
try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
    print("API Mode Enabled - Real-time prices via Yahoo Finance")
except ImportError:
    YFINANCE_AVAILABLE = False
    print("Offline Mode - Predefined prices used")
    print("To use real-time prices, install yfinance: pip install yfinance")

class Stock:
    """
    Represents an individual stock with its symbol and price.
    """
    def __init__(self, symbol, fallback_price=100.0):
        if not isinstance(symbol, str) or not symbol:
            raise ValueError("Stock symbol must be a non-empty string.")
        self.symbol = symbol.upper()
        self.fallback_price = fallback_price
        self._price = None

    @property
    def price(self):
        if self._price is None:
            self.fetch_price()
        return self._price

    def fetch_price(self):
        """Fetches stock price via API or uses a fallback price."""
        if YFINANCE_AVAILABLE:
            try:
                ticker = yf.Ticker(self.symbol)
                todays_data = ticker.history(period="1d")
                if not todays_data.empty:
                    self._price = float(todays_data["Close"].iloc[-1])
                    print(f"Price fetched for {self.symbol}: {self._price:.2f}€")
                else:
                    self._price = self.fallback_price
                    print(f"No data found for {self.symbol}. Using fallback price: {self._price:.2f}€")
            except Exception as e:
                self._price = self.fallback_price
                print(f"Error fetching price for {self.symbol}: {e}")
                print(f"Using fallback price: {self._price:.2f}€")
        else:
            # Predefined prices if yfinance is not available
            predefined_prices = {
                "AAPL": 180.0,
                "MSFT": 250.0,
                "GOOG": 120.0,
                "AMZN": 100.0,
                "TSLA": 220.0,
                "NVDA": 400.0,
                "META": 300.0
            }
            self._price = predefined_prices.get(self.symbol, self.fallback_price)
            print(f"Predefined price for {self.symbol}: {self._price:.2f}€")

    def __str__(self):
        return f"{self.symbol} (Price: {self.price:.2f}€)"

class Portfolio:
    """
    Manages a stock portfolio.
    """
    def __init__(self):
        self.holdings = {}
        self.stocks_in_portfolio = {}

    def add_holding(self, symbol, quantity):
        """Adds a position to the portfolio."""
        if not isinstance(symbol, str) or not symbol:
            raise ValueError("Stock symbol must be a non-empty string.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        symbol = symbol.upper()
        if symbol not in self.stocks_in_portfolio:
            self.stocks_in_portfolio[symbol] = Stock(symbol)

        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        print(f"✓ {quantity} shares of {symbol} added to your portfolio.")

    def calculate_total_investment(self):
        """Calculates the total value of the portfolio."""
        total_value = 0.0
        investment_details = []

        print("\n" + "="*50)
        print("YOUR PORTFOLIO DETAILS")
        print("="*50)
        
        if not self.holdings:
            print("Your portfolio is empty.")
            return 0.0, []

        for symbol, quantity in self.holdings.items():
            stock = self.stocks_in_portfolio.get(symbol)
            if stock and stock.price > 0:
                value = quantity * stock.price
                total_value += value
                detail_str = f"{stock.symbol}: {quantity} shares @ {stock.price:.2f}€ = {value:.2f}€"
                print(detail_str)
                investment_details.append([stock.symbol, quantity, stock.price, value])
            else:
                detail_str = f"{symbol}: Price not available. Not included in total."
                print(detail_str)
                investment_details.append([symbol, quantity, 'N/A', 'N/A'])

        print("-" * 50)
        print(f"TOTAL INVESTMENT VALUE: {total_value:.2f}€")
        print("=" * 50)
        return total_value, investment_details

    def save_to_csv(self, total_value, investment_details, filename='portfolio_summary.csv'):
        """Saves results to a CSV file."""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Stock', 'Quantity', 'Unit Price (€)', 'Total Value (€)'])
                writer.writerows(investment_details)
                writer.writerow([])
                writer.writerow(['Total Portfolio Value', '', '', f'{total_value:.2f}€'])
            print(f"✓ Results saved to '{filename}'.")
        except IOError as e:
            print(f"✗ Error saving file: {e}")

def get_user_input_portfolio(portfolio_manager):
    """User input interface."""
    print("\n" + "="*50)
    print("ENTER YOUR STOCK PORTFOLIO")
    print("="*50)
    print("Instructions:")
    print("- Enter stock symbol (e.g., AAPL, MSFT, GOOG)")
    print("- Enter 'fin' at any time to finish")
    print("-" * 50)

    while True:
        try:
            symbol = input("\nStock Symbol: ").strip()
            if symbol.lower() == 'fin':
                break
            if not symbol:
                print("⚠ Symbol cannot be empty. Please try again.")
                continue

            quantity_str = input(f"Quantity of {symbol.upper()}: ").strip()
            if quantity_str.lower() == 'fin':
                break
            
            quantity = int(quantity_str)
            if quantity <= 0:
                print("⚠ Quantity must be a positive number.")
                continue
                
            portfolio_manager.add_holding(symbol, quantity)
            
        except ValueError:
            print("⚠ Invalid quantity. Please enter a positive integer.")
        except KeyboardInterrupt:
            print("\n\nUser interruption. Exiting program.")
            sys.exit(0)
        except Exception as e:
            print(f"⚠ An unexpected error occurred: {e}")

def main():
    """Main function."""
    print("="*60)
    print("    PROFESSIONAL STOCK PORTFOLIO TRACKER")
    print("="*60)
    
    try:
        # Initialize portfolio
        portfolio_manager = Portfolio()

        # Get user input for portfolio
        get_user_input_portfolio(portfolio_manager)

        # Calculate and display total value
        total_value, investment_details = portfolio_manager.calculate_total_investment()

        # Save option
        if investment_details:
            print("\n" + "-"*50)
            save_option = input("Do you want to save the results to a CSV file? (yes/no): ").strip().lower()
            if save_option in ['oui', 'o', 'yes', 'y']:
                portfolio_manager.save_to_csv(total_value, investment_details)
            else:
                print("Results will not be saved.")
        else:
            print("No investment details to save.")

        print("\n" + "="*60)
        print("Thank you for using the Stock Portfolio Tracker!")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"\nFatal error: {e}")
        print("Program will exit.")

if __name__ == "__main__":
    main()

