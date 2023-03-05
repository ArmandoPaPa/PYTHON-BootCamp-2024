# Age Calculator Exercise

age = input("Enter your age in numbers (in years): ")

print("Your age in days is: " + str((float(age) * 365)) + " days")
print(f"Your age in days is: {float(age) * 365} days")

print("-" * 23)


# Shopping Cart Exercise

print("WELCOME TO OUR STORE!")
item = input("What item are you purchasing? ")
price = float(input(f"What is the price of {item}? "))
quantity = float(input(f"How many {item}(s) are you buying? "))

print("*" * 23)
print(f"Added {quantity} {item}(s) to shopping cart...")
print(f"Subtotal: $ {price * quantity}")
