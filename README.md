# CodeAlpha Python Programming Internship Projects

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CodeAlpha](https://img.shields.io/badge/CodeAlpha-Internship-orange.svg)](https://codealpha.tech/)

## 🌟 Welcome to My CodeAlpha Python Programming Internship Projects!

This repository showcases my work during the **CodeAlpha Python Programming Internship**. It contains two distinct projects, each designed to challenge and enhance fundamental Python programming skills, object-oriented design, and practical application development.

--- 

## 🎮 Task 1: Hangman Game

### Overview

A classic text-based Hangman game where the player guesses a hidden word letter by letter within a limited number of incorrect attempts. This task focuses on core Python concepts such as loops, conditionals, string manipulation, and list handling.

### ✨ Features

-   **Text-Based Interface**: Simple and interactive command-line gameplay.
-   **Predefined Word List**: Uses a small, hardcoded list of words for guessing.
-   **Limited Guesses**: Players have a set number of incorrect guesses (6 attempts).
-   **Basic Input/Output**: Handles user input and displays game state (e.g., guessed letters, remaining attempts, word progress) via the console.

### 🚀 Getting Started (Task 1)

#### Prerequisites

-   Python 3.x

#### Installation

1.  **Navigate to the Task 1 directory:**
    ```bash
    cd Task1-hangman_game
    ```

#### Usage

1.  **Run the game:**
    ```bash
    python main.py
    ```

2.  **Play the game:**
    Follow the on-screen instructions to guess letters and uncover the hidden word.

### 🛠️ Technical Implementation (Task 1)

-   **`random` module**: For selecting a word.
-   **`while` loops**: For game flow.
-   **`if-else` statements**: For conditional logic.
-   **Strings & Lists**: For data handling and game state.

---

## 📈 Task 2: Stock Portfolio Tracker

### Overview

A professional command-line application for tracking your stock portfolio. It allows users to input stock symbols and quantities, then calculates the total investment value by fetching real-time stock prices. This project emphasizes object-oriented design, API integration, and robust error handling.

### ✨ Features

-   **Real-time Stock Prices**: Integrates with Yahoo Finance API via `yfinance` library for up-to-date stock prices.
-   **Offline Mode**: Gracefully falls back to predefined stock prices when API is unavailable or `yfinance` is not installed.
-   **Object-Oriented Design**: Clean, modular code structure using `Stock` and `Portfolio` classes.
-   **Robust Input Validation**: Handles invalid user inputs (e.g., non-numeric quantities, empty symbols) with clear error messages.
-   **Detailed Investment Summary**: Displays a clear breakdown of each stock holding and the total portfolio value.
-   **CSV Export**: Option to save the portfolio summary to a CSV file for easy record-keeping and further analysis.
-   **User-Friendly Interface**: Provides clear instructions and feedback to the user throughout the process.

### 🚀 Getting Started (Task 2)

#### Prerequisites

-   Python 3.x
-   `pip` (Python package installer)

#### Installation

1.  **Navigate to the Task 2 directory:**
    ```bash
    cd Task2-StockPortfolioTracker
    ```

2.  **Install required Python packages:**
    ```bash
    pip install yfinance
    ```
    *Note: If you don't install `yfinance`, the application will use predefined stock prices.*

#### Usage

1.  **Run the application:**
    ```bash
    python main.py
    ```

2.  **Follow the interactive prompts:**
    -   Enter stock symbols (e.g., AAPL, MSFT, GOOG, TSLA)
    -   Enter the quantity of shares for each stock
    -   Type `fin` when you're done adding stocks
    -   Choose whether to save results to CSV

### 🛠️ Technical Implementation (Task 2)

-   **Object-Oriented Programming (OOP)**: Classes (`Stock`, `Portfolio`) for better code organization.
-   **API Integration**: Real-time data fetching using `yfinance`.
-   **Error Handling**: Try-catch blocks for robust error management.
-   **File I/O**: CSV file generation for data persistence.
-   **User Input Validation**: Ensuring data integrity and user experience.

## 📁 Global Project Structure

```
CodeAlpha-PythonProgramming/
├── Task1-hangman_game/
│   └── main.py             # Main game logic for Hangman
│   └── README.md           # README for Task 1
├── Task2-StockPortfolioTracker/
│   └── main.py             # Main application script for Stock Tracker
│   └── portfolio_summary.csv # Example output CSV (generated after running)
│   └── README.md           # README for Task 2
└── README.md               # This global documentation file
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

-   **CodeAlpha** for providing the internship opportunity.
-   **Yahoo Finance** for stock data API.
-   **yfinance** library developers for the Python wrapper.

## 📞 Contact

-   **GitHub**: [@hamzakh86](https://github.com/hamzakh86)
-   **Project Repository**: [CodeAlpha-PythonProgramming](https://github.com/hamzakh86/CodeAlpha-PythonProgramming)

---

*This repository contains projects developed during the CodeAlpha Python Programming Internship.*

