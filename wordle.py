from curses.ascii import isalpha
from requests import get
import string
from valid_words import valid_words
from colorama import Fore, Style
from random import choice
# Colorama - allows use of colors, Requests - allows you to sent HTTP requests.
print("""Guess the WORDLE in 6 tries. 
Each guess must be a valid 5-letter word. Hit the enter key to submit.
After each guess, the color of the tiles will change to show how close your
guess was to the word.""")
print("-" * 79)

def play_wordle():

    print(Fore.BLUE + 'Guess a 5 letter word to begin!' + Style.RESET_ALL)
    print('\n')

    word = choice(valid_words).upper()
    guesses = 6
    letters = string.ascii_uppercase
    correct_letters = ''
    semi_correct_letters = ''
    wrong_letters = ''

    while guesses:
        player_guess = input().upper()
        display = ''
        guessed_letters = ''
# isalpha() - returns True if aall the characters are alphabet letters (a-z).
        if len(player_guess) != 5:
            print(Fore.RED + 'Enter a valid 5 letter word.' + Style.RESET_ALL)
            continue
        if not player_guess.isalpha():
            print(Fore.RED + 'Enter a valid 5 letter word.' + Style.RESET_ALL)
            continue

        for i in range(len(word)):
            if player_guess[i] == word[i]:
                display += Fore.GREEN + player_guess[i] + Style.RESET_ALL
                correct_letters += player_guess[i]
            elif player_guess[i] in word:
                display += Fore.YELLOW + player_guess[i] + Style.RESET_ALL
                semi_correct_letters += player_guess[i]
            elif player_guess[i] not in word:
                display += Fore.RED + player_guess[i] + Style.RESET_ALL
                wrong_letters += player_guess[i]

        for i in range(len(letters)):
            if letters[i] in correct_letters:
                guessed_letters += Fore.GREEN + letters[i] + Style.RESET_ALL
            elif letters[i] in semi_correct_letters:
                guessed_letters += Fore.YELLOW + letters[i] + Style.RESET_ALL
            elif letters[i] in wrong_letters:
                guessed_letters += Fore.RED + letters[i] + Style.RESET_ALL
            else:
                guessed_letters += letters[i]

        print(
            "\033[A                                                            \033[A")
        print(
            "\033[A                                                            \033[A")
        print('[', guesses, ']', display)
        print('[ Guessed: ]', guessed_letters)

        guesses -= 1

        if player_guess == word:
            print(Fore.BLUE + 'You guessed the word!' + Style.RESET_ALL)
            break
        if guesses == 0:
            print(
                Fore.RED + 'You failed to guess the word, try again next time!' + Style.RESET_ALL)
            print(Fore.MAGENTA + 'The correct word was', word + Style.RESET_ALL)

playing = True
while True:
    print(Fore.BLUE + "Start a game of Wordle? (y/n)" + Style.RESET_ALL)
    response = input().lower()

    print('\n')

    if response == "n":
        playing = False
        break
    elif response == "y":
        play_wordle()