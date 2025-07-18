# CodeAlpha Python Programming - Task 2: Stock Portfolio Tracker

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CodeAlpha](https://img.shields.io/badge/CodeAlpha-Internship-orange.svg)](https://codealpha.tech/)

## 📋 Project Overview

This project is part of the **CodeAlpha Python Programming Internship** program. The Stock Portfolio Tracker is a professional command-line application that allows users to track their stock investments by calculating the total portfolio value based on real-time stock prices.

## ✨ Features

- **Real-time Stock Prices**: Integrates with Yahoo Finance API via `yfinance` library for up-to-date stock prices
- **Offline Mode**: Gracefully falls back to predefined stock prices when API is unavailable
- **Object-Oriented Design**: Clean, modular code structure using `Stock` and `Portfolio` classes
- **Robust Input Validation**: Handles invalid user inputs with clear error messages
- **Detailed Portfolio Summary**: Shows breakdown of each stock holding and total portfolio value
- **CSV Export**: Save portfolio summary to CSV file for record-keeping
- **User-Friendly Interface**: Clear instructions and feedback throughout the process
- **Error Handling**: Comprehensive error handling for API failures and user input errors

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hamzakh86/CodeAlpha-PythonProgramming.git
   cd CodeAlpha-PythonProgramming/Task2-StockPortfolioTracker
   ```

2. **Install required dependencies:**
   ```bash
   pip install yfinance
   ```
   *Note: If you don't install `yfinance`, the application will use predefined stock prices.*

### Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Follow the interactive prompts:**
   - Enter stock symbols (e.g., AAPL, MSFT, GOOG, TSLA)
   - Enter the quantity of shares for each stock
   - Type 'fin' when you're done adding stocks
   - Choose whether to save results to CSV

### Example Usage

```
============================================================
    PROFESSIONAL STOCK PORTFOLIO TRACKER
============================================================
API Mode Enabled - Real-time prices via Yahoo Finance

==================================================
ENTER YOUR STOCK PORTFOLIO
==================================================
Instructions:
- Enter stock symbol (e.g., AAPL, MSFT, GOOG)
- Enter 'fin' at any time to finish
--------------------------------------------------

Stock Symbol: AAPL
Quantity of AAPL: 10
✓ 10 shares of AAPL added to your portfolio.

Stock Symbol: MSFT
Quantity of MSFT: 5
✓ 5 shares of MSFT added to your portfolio.

Stock Symbol: fin

==================================================
YOUR PORTFOLIO DETAILS
==================================================
Price fetched for AAPL: 180.50€
AAPL: 10 shares @ 180.50€ = 1805.00€
Price fetched for MSFT: 250.75€
MSFT: 5 shares @ 250.75€ = 1253.75€
--------------------------------------------------
TOTAL INVESTMENT VALUE: 3058.75€
==================================================

Do you want to save the results to a CSV file? (yes/no): yes
✓ Results saved to 'portfolio_summary.csv'.
```

## 📁 Project Structure

```
Task2-StockPortfolioTracker/
├── main.py                 # Main application script
├── portfolio_summary.csv   # Example output CSV (generated after running)
└── README.md              # This documentation file
```

## 🛠️ Technical Implementation

### Classes

- **`Stock`**: Represents individual stocks with symbol and price fetching capabilities
- **`Portfolio`**: Manages the collection of stocks and calculates total portfolio value

### Key Concepts Used

- **Object-Oriented Programming (OOP)**: Classes and methods for better code organization
- **API Integration**: Real-time data fetching using `yfinance`
- **Error Handling**: Try-catch blocks for robust error management
- **File I/O**: CSV file generation for data persistence
- **User Input Validation**: Ensuring data integrity and user experience

## 📊 Sample Output

The application generates a CSV file with the following structure:

| Stock | Quantity | Unit Price (€) | Total Value (€) |
|-------|----------|----------------|-----------------|
| AAPL  | 10       | 180.50         | 1805.00         |
| MSFT  | 5        | 250.75         | 1253.75         |
|       |          |                |                 |
| **Total Portfolio Value** |  |    | **3058.75€**    |

## 🔧 Requirements Met

This project fulfills all requirements of **CodeAlpha Task 2**:

- ✅ User inputs stock names and quantities
- ✅ Uses hardcoded dictionary for stock prices (with API enhancement)
- ✅ Displays total investment value
- ✅ Optional CSV file saving
- ✅ Utilizes key concepts: dictionaries, input/output, arithmetic, file handling

## 🌟 Enhancements Beyond Basic Requirements

- Real-time API integration for current stock prices
- Professional object-oriented code structure
- Comprehensive error handling and input validation
- Enhanced user interface with clear formatting
- Detailed documentation and comments

## 🤝 Contributing

This project is part of the CodeAlpha internship program. Suggestions and improvements are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CodeAlpha** for providing the internship opportunity
- **Yahoo Finance** for stock data API
- **yfinance** library developers for the Python wrapper

## 📞 Contact

- **GitHub**: [@hamzakh86](https://github.com/hamzakh86)
- **Project Repository**: [CodeAlpha-PythonProgramming](https://github.com/hamzakh86/CodeAlpha-PythonProgramming)

---

*This project is part of the CodeAlpha Python Programming Internship - Task 2*

