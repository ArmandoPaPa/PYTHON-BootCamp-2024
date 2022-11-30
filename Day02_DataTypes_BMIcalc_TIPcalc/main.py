# print("Hello"[0])
# print("123" + "456")
# print(123 + 456)
# print("--------------------------------")


# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# # print("Your name has " + num_char + " characters.") <- does not work
# print("Your name has " + new_num_char + " characters.")
# print(type(num_char))
# print("--------------------------------")


# # Data types
# two_digit_number = input("Enter a two digit number: ")
# print(int(two_digit_number[0]) + int(two_digit_number[1]))
# print("--------------------------------")


# # BMI Calculator
# print("Hi! Let us calculate your BMI!")
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# print("Your BMI is:")
# print(int(float(weight)/(float(height)**2)))
# print("--------------------------------")


# # Life in weeks left until 90yrs
#
# print("If a person can live up to 90 yrs,\n   how many DAYS, WEEKS, and MONTHS are left for you!?")
# age = input("What is your current age? ")
#
# years_left = 90 - int(age)
# months_left = years_left * 12
# weeks_left = years_left * 52
# days_left = years_left * 365
#
# print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


# Project: Tip Calculator

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
total_bill_as_float = float(total_bill)
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_percentage_as_float = float(tip_percentage) / 100
people = input("How many people to split the bill? ")
people_as_int = int(people)

# each_person_pay = round(total_bill_as_float * (1 + tip_percentage_as_float) / people_as_int, 2)
# print(f"Each person should pay: ${each_person_pay}")

each_person_pay = "{:.2f}".format(total_bill_as_float * (1 + tip_percentage_as_float) / people_as_int, 2)
print(f"Each person should pay: ${each_person_pay}")
