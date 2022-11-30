# # Loops
#
# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")


# # Average student height
#
# student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# counter = 0
# total_height = 0
# for student in student_heights:
#     total_height += student
#     counter += 1
#
# print(round(total_height / counter))


# # Average score
#
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# highest_score = 0
#
# for score in student_scores:
#     if highest_score < score:
#         highest_score = score
#
# print(f"The highest score in the class is: {highest_score}")


# # For Loop with Range
#
# for number in range(1, 10, 3):
#     print(number)
#
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# # 1-100 sum of even numbers
#
# sum_of_even_numbers = 0
# for number in range(2, 101, 2):
#     sum_of_even_numbers += number
# print(sum_of_even_numbers)


# # FizzBuzz
#
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

py_psw_list = []

for char in range(0, nr_letters):
    py_psw_list += random.choice(letters)

for char in range(0, nr_symbols):
    py_psw_list += random.choice(symbols)

for char in range(0, nr_numbers):
    py_psw_list += random.choice(numbers)

print(py_psw_list)
random.shuffle(py_psw_list)
print(py_psw_list)

psw = ""
for char in py_psw_list:
    psw += char

print(f"Your password is: {psw}")
