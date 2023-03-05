print("WELCOME to BMI Calculus!")

weight_in_pounds = float(input("Enter your WEIGHT in POUNDS:   "))
height_in_inches = float(input("Enter your HEIGHT in INCHES:   "))

bmi = (weight_in_pounds * 703) / (height_in_inches ** 2)

if bmi > 39.9:
    print("Morbidly Obese")
elif bmi >= 35.0:
    print("Severely Obese")
elif bmi >= 30:
    print("Moderately Obese")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
elif bmi >= 16:
    print("Underweight")
elif bmi >= 0:
    print("Severely Underweight")
else:
    print("Sorry, something gone wrong!")

