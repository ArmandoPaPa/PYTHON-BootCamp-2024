import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)
# rnd_0_to_5 = random_float * 5
# print(rnd_0_to_5)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")


# # Heads or Tails -> 1 means Heads / 0 means Tails
# heads_or_tails = random.randint(0, 1)
# if heads_or_tails == 1:
#     print("Heads")
# else:
#     print("Tails")


# states_of_america = ["Delaware", "Pennsylvania", "etc"]
# print(states_of_america[0])
# states_of_america[2] = "Etc."
# states_of_america.append("Russia ;)")
# states_of_america.extend(["x", "y", "z"])
# print(states_of_america)


# # Banker Roulette
#
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# rnd = random.randint(0, len(names) - 1)
# print(f"{names[rnd]} is going to buy the meal today!")
# print(f"{random.choice(names)} -> alternative using .choice(names)")


# some_list = ["a", "b", "c", "...", "x", "y", "z"]
#
# print(len(some_list))
# # be mindful of -1!
#
# print(some_list)


# # List within a list = Nested Lists
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# some_mix = [fruits, vegetables]
#
# print(some_mix)


# # Treasure Map
#
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# pos_horizontal = int(position[0])
# pos_vertical = int(position[1])
#
# map[pos_vertical - 1][pos_horizontal - 1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")


# Rock Paper Scissors


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

playerChoice = input("What do you choose?\nType 0 for ROCK, 1 for PAPER or 2 for SCISSORS.\n")

if playerChoice == "0":
    print(rock)
if playerChoice == "1":
    print(paper)
if playerChoice == "2":
    print(scissors)

computerChoice = random.randint(0, 2)
print("\nComputer chose:\n")

if computerChoice == 0:
    print(rock)
if computerChoice == 1:
    print(paper)
if computerChoice == 2:
    print(scissors)

if playerChoice == "0":
    if computerChoice == 0:
        print("DRAW")
    elif computerChoice == 1:
        print("You LOSE")
    elif computerChoice == 2:
        print("You WIN! Congrats!")
elif playerChoice == "1":
    if computerChoice == 0:
        print("You WIN! Congrats!")
    elif computerChoice == 1:
        print("DRAW")
    elif computerChoice == 2:
        print("You LOSE")
elif playerChoice == "2":
    if computerChoice == 0:
        print("You LOSE")
    elif computerChoice == 1:
        print("You WIN! Congrats!")
    elif computerChoice == 2:
        print("DRAW")
else:
    print("Sorry, something went wrong! Most probably you did not choose: 0, 1 or 2")
