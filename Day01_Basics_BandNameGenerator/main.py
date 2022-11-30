print("Hello World!")
print("-------------------")

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
print("-------------------")

print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")
print("-------------------")

print("Hello" + " Angela")
print("-------------------")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
print("-------------------")

print("Hello " + input("What is your name?\n") + "!")
print("-------------------")

print(len(input("What is your name? ")))
print("-------------------")

name = input("What is your name?\n")
print(name)
length = len(name)
print(length)
print("-------------------")

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

print("-------------------")


# Band Name Generator
print("Let us try help you generate your Band Name! ;)")
String_city = input("What's name?\n")
String_pets_name = input("What's your pet's name?\n")
print("\nHi! Your Band Name could be = " + String_city + " " + String_pets_name)
