# print("Welcome to the roller-coaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride!")
# else:
#     print("Not today! You need to grow taller!")


# # Odd or Even
# number = int(input("Which number do you want to check to be Odd or Even? "))
#
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


# print("Welcome to the roller-coaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride!")
#     age = int(input("What is your age? "))
#     if age >= 18:
#         print("You should buy an adult ticket and pay: $12.00")
#     elif 18 > age >= 12:
#         print("You should buy a teenager ticket and pay: $7.00")
#     else:
#         print("Your ticket price is: $5.00")
# else:
#     print("Not today! You need to grow taller!")


# # BMI calculation
# print("Let us calculate your BMI!")
#
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# bmi = int(round((weight / height ** 2), 0))
#
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif 18.5 <= bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif 25 <= bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif 30 <= bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")


# # Leap year
# print("Let us determine - Leap year OR not!")
#
# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 400 == 0:
#         print("Leap year.")
#     elif year % 100 == 0:
#         print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")


# print("Welcome to the roller-coaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride!")
#     age = int(input("What is your age? "))
#     if age >= 18:
#         print("Adult tickets are: $12.00")
#         bill = 12
#     elif 18 > age >= 12:
#         print("Youth tickets are: $7.00")
#         bill = 7
#     else:
#         print("Child tickets: $5.00")
#         bill = 5
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"You have to pay ${bill}. Ty.")
#
# else:
#     print("Not today! You need to grow taller!")


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# bill = 0
#
# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# elif size == "L":
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# else:
#     print("You have not chosen anything. See you next time!")
#
# print(f"Your final bill is: ${bill}.")


# print("Welcome to the roller-coaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride!")
#     age = int(input("What is your age? "))
#     if age >= 45 and age <= 55:
#         print("You can ride for free!")
#     elif age >= 18:
#         print("Adult tickets are: $12.00")
#         bill = 12
#     elif 18 > age >= 12:
#         print("Youth tickets are: $7.00")
#         bill = 7
#     else:
#         print("Child tickets: $5.00")
#         bill = 5
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"You have to pay ${bill}. Ty.")
#
# else:
#     print("Not today! You need to grow taller!")


# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# name1_lowerCase = name1.lower()
# name2_lowerCase = name2.lower()
#
#
# T_count = name1_lowerCase.count("t") + name2_lowerCase.count("t")
# R_count = name1_lowerCase.count("r") + name2_lowerCase.count("r")
# U_count = name1_lowerCase.count("u") + name2_lowerCase.count("u")
# E_count = name1_lowerCase.count("e") + name2_lowerCase.count("e")
#
# L_count = name1_lowerCase.count("l") + name2_lowerCase.count("l")
# O_count = name1_lowerCase.count("o") + name2_lowerCase.count("o")
# V_count = name1_lowerCase.count("v") + name2_lowerCase.count("v")
# E_count = name1_lowerCase.count("e") + name2_lowerCase.count("e")
#
# true_number = T_count + R_count + U_count + E_count
# love_number = L_count + O_count + V_count + E_count
#
# score_string = str(true_number) + str(love_number)
# score_number = int(score_string)
#
#
# if score_number < 10 or score_number > 90:
#     print(f"Your score is {score_number}, you go together like coke and mentos.")
# elif score_number >= 40 and score_number <= 50:
#     print(f"Your score is {score_number}, you are alright together.")
# else:
#     print(f"Your score is {score_number}.")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Would you like to go 'left' or 'right'? ").lower()

if direction == "right":
    print("Game Over.")
elif direction == "left":
    swim_or_wait = input("Would you like to 'swim' or 'wait'? ").lower()
    if swim_or_wait == "swim":
        print("Game Over.")
    elif swim_or_wait == "wait":
        door = input("Which door do you want to go: 'Red', 'Blue', 'Yellow'? ").lower()
        if (door == "red") or (door == "blue"):
            print("Game Over.")
        elif door == "yellow":
            print("YOU WIN!!!")
        else:
            print("You typed something wrong! Game Over.")
    else:
        print("You typed something wrong! Game Over.")
else:
    print("You typed something wrong! Game Over.")
