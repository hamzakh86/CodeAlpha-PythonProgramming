# Hangman Game - CodeAlpha Internship Project

import random
from colorama import init

def main():
    init()
    welcome = [
        '\033[1;34mWelcome to \033[1;31mHangman\033[0m\033[1;34m! - CodeAlpha Python Internship',
        'Try to guess the hidden word one letter at a time.',
        'You have 6 incorrect attempts allowed. \033[1;33mGood luck!\033[0m'
    ]

    for line in welcome:
        print(line)

    play_again = True

    while play_again:
        # Reduced to 5 words as per task requirements
        words = ["hangman", "intern", "codealpha",
                 "computer", "python", "program", "programming",
                 "science", "internship", "coding",
                    "developer", "software", "engineer", "algorithm"
                 ]
        chosen_word = random.choice(words).lower()
        guessed_letters = []
        word_guessed = ["-" for _ in chosen_word]
        attempts = 6

        while attempts > 0 and "-" in word_guessed:
            print(f"\033[1;31m\nAttempts left: {attempts}")
            print("\033[1;34mCurrent word: " + "".join(word_guessed))

            try:
                player_guess = input("\033[1;37m\nGuess a letter: ").lower()
                
                if not player_guess.isalpha() or len(player_guess) != 1:
                    print("\033[1;33mPlease enter a single letter.")
                    continue
                if player_guess in guessed_letters:
                    print("\033[1;33mYou already guessed that letter.")
                    continue
                    
            except:
                print("\033[1;33mInvalid input. Please try again.")
                continue

            guessed_letters.append(player_guess)

            if player_guess in chosen_word:
                for i, letter in enumerate(chosen_word):
                    if letter == player_guess:
                        word_guessed[i] = player_guess
            else:
                attempts -= 1
                print("\033[1;31mIncorrect guess!")

        if "-" not in word_guessed:
            print(f"\n\033[1;32mCongratulations! You won! The word was {chosen_word}")
        else:
            print(f"\n\033[1;31mGame over! The word was {chosen_word}")

        response = input("\n\033[1;37mPlay again? (yes/no): ").lower()
        if response not in ("yes", "y", "yeah", "yep"):
            play_again = False
            print("\033[1;34mThank you for playing Hangman - CodeAlpha Project!")

if __name__ == "__main__":
    main()