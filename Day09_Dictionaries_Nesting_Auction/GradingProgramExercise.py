student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

# This is the scoring criteria:
#
# Scores 91 - 100: Grade = "Outstanding"
#
# Scores 81 - 90: Grade = "Exceeds Expectations"
#
# Scores 71 - 80: Grade = "Acceptable"
#
# Scores 70 or lower: Grade = "Fail"

for student in student_scores:
    if 91 <= student_scores[student] <= 100:
        student_grades[student] = "Grade = \"Outstanding\""
    elif 81 <= student_scores[student] <= 90:
        student_grades[student] = "Grade = \"Exceeds Expectations\""
    elif 71 <= student_scores[student] <= 80:
        student_grades[student] = "Grade = \"Acceptable\""
    elif 0 <= student_scores[student] <= 70:
        student_grades[student] = "Grade = \"Fail\""
    else:
        print("Something went wrong! Ups!")


# 🚨 Don't change the code below 👇

print(student_grades)
