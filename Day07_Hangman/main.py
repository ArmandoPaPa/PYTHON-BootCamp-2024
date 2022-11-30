import random

import hangman_art
import hangman_words

print(hangman_art.logo)

word_to_guess = random.choice(hangman_words.word_list)
word_to_guess_array = list(word_to_guess)
display = []

for number in range(0, len(word_to_guess_array)):
    display.append("_")

lives = len(hangman_art.stages)
word_guessed = False

print(hangman_art.stages[lives - 1])

for number in range(0, len(display)):
    print(display[number] + " ", end="")
print()

while lives != 1 and not word_guessed:

    user_letter_guess = input("Please, guess a letter! ").lower()

    letter_guessed = False

    for number in range(0, len(word_to_guess_array)):
        if user_letter_guess == word_to_guess_array[number]:
            display[number] = user_letter_guess
            letter_guessed = True

    if not letter_guessed:
        lives -= 1
        print(hangman_art.stages[lives - 1])
        print(f"You guessed a letter '{user_letter_guess}' "
              f"and it is not in the word. You lose a life.")

    for number in range(0, len(word_to_guess_array)):
        if display[number] == word_to_guess_array[number]:
            word_guessed = True
        else:
            word_guessed = False
            break

    for number in range(0, len(display)):
        print(display[number] + " ", end="")
    print()

if word_guessed:
    print("You WON! Congratulations!")
else:
    print("You LOOSE, sorry!")
    print(f"You should have guessed word '{word_to_guess}'")
