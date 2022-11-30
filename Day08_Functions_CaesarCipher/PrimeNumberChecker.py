def prime_checker(number):
    prime_number = "It's a prime number."
    not_prime_number = "It's not a prime number."
    is_prime_number = True

    if number <= 0:
        print("Please enter a whole number larger than 0!")
    else:
        if number == 1 or number == 2:
            print(f"Number: {number} = {prime_number}")
        else:
            for n in range(2, number):
                if number % n == 0:
                    print(f"Number: {number} = {not_prime_number}")
                    is_prime_number = False
                    break

            if is_prime_number:
                print(f"Number: {number} = {prime_number}")


print("PRIME CHECKER! Please, choose a whole number larger than 0 to check!")
n = int(input("Check this number: "))

prime_checker(number=n)
