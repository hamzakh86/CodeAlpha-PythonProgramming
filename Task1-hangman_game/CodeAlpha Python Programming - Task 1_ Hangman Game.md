# CodeAlpha Python Programming - Task 1: Hangman Game

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CodeAlpha](https://img.shields.io/badge/CodeAlpha-Internship-orange.svg)](https://codealpha.tech/)

## 📋 Project Overview

This project is part of the **CodeAlpha Python Programming Internship** program. It implements a classic text-based Hangman game, where the player tries to guess a hidden word by suggesting letters within a limited number of incorrect attempts. This task focuses on fundamental Python programming concepts such as loops, conditionals, string manipulation, and list handling.

## ✨ Features

- **Text-Based Interface**: Simple and interactive command-line gameplay.
- **Predefined Word List**: Uses a small, hardcoded list of words for guessing.
- **Limited Guesses**: Players have a set number of incorrect guesses (6 attempts).
- **Basic Input/Output**: Handles user input and displays game state (e.g., guessed letters, remaining attempts, word progress) via the console.

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository (or download the files):**
   ```bash
   git clone https://github.com/hamzakh86/CodeAlpha-PythonProgramming.git
   cd CodeAlpha-PythonProgramming/Task1-hangman_game
   ```
   *(Assuming `Task1-hangman_game` is the directory for this project within your main repository)*

### Usage

1. **Run the game:**
   Navigate to the project directory in your terminal and execute the `main.py` script (or whatever your main game file is named, e.g., `hangman.py`):

   ```bash
   python main.py
   ```

2. **Play the game:**
   Follow the on-screen instructions. You will be prompted to guess letters one by one. The game will inform you if your guess is correct or incorrect, and show the current state of the word and your remaining guesses.

### Example Gameplay (Illustrative)

```
Welcome to Hangman!
Guess the word:
_ _ _ _ _

You have 6 incorrect guesses remaining.

Enter a letter: a
Good guess!
_ A _ _ _

You have 6 incorrect guesses remaining.

Enter a letter: z
Incorrect guess!
_ A _ _ _

You have 5 incorrect guesses remaining.

Enter a letter: p
Good guess!
_ A P P _

You have 5 incorrect guesses remaining.

...
```

## 📁 Project Structure

```
Task1-hangman_game/
├── main.py                 # Main game logic
└── README.md               # This documentation file
```

## 🛠️ Technical Implementation

### Key Concepts Used

- **`random` module**: For selecting a word from the predefined list.
- **`while` loops**: To control the game flow (e.g., main game loop, input loop).
- **`if-else` statements**: For conditional logic (e.g., checking guesses, win/loss conditions).
- **Strings**: For handling words, letters, and displaying game state.
- **Lists**: For storing the word list, guessed letters, and managing the hidden word progress.
- **Basic Input/Output**: `input()` for user guesses and `print()` for displaying information.

## 📊 Game Scope

As per the internship task requirements, this implementation adheres to a simplified scope:

- Uses a small list of 5 predefined words.
- Limits incorrect guesses to 6.
- Features basic console input/output without graphics or audio.

## 🤝 Contributing

This project is part of the CodeAlpha internship program. Suggestions for improvements or bug fixes are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CodeAlpha** for providing the internship opportunity.

## 📞 Contact

- **GitHub**: [@hamzakh86](https://github.com/hamzakh86)
- **Project Repository**: [CodeAlpha-PythonProgramming](https://github.com/hamzakh86/CodeAlpha-PythonProgramming)

---

*This project is part of the CodeAlpha Python Programming Internship - Task 1*

