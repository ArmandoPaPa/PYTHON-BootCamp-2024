import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number_to_guess = random.randint(1, 100)

difficulty = None
while difficulty != "easy" and difficulty != "hard":
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':   ")

if difficulty == "easy":
    counter = EASY_LEVEL_TURNS

if difficulty == "hard":
    counter = HARD_LEVEL_TURNS


def guess(_guess_number, _number_to_guess):
    if _guess_number > _number_to_guess:
        print("Too high.")
        return False
    elif _guess_number < _number_to_guess:
        print("Too low.")
        return False
    elif _guess_number == _number_to_guess:
        print(f"Congrats! You guessed the number: {_number_to_guess}")
        return True
    else:
        print("Sorry, something went wrong!")
        return False


you_guessed_the_number = False

while counter != 0 and you_guessed_the_number is False:
    print(f"You have {counter} attempts remaining to guess the number.")
    your_guess = int(input("Make a guess:   "))
    counter -= 1
    you_guessed_the_number = guess(your_guess, number_to_guess)

if counter == 0 and you_guessed_the_number is False:
    print(f"Sorry! You did not guess the number! It was {number_to_guess}")
