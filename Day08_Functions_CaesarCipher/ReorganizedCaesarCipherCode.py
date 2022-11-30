import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(art.logo)

print("Hi! Welcome to Caesar Cipher!")


def caesar_cipher(chosen_action, input_text, shift_number):
    text_to_work_with_lower_case = input_text.lower()
    crypto_text = ""

    for char_index in range(0, len(text_to_work_with_lower_case)):
        char_tested = text_to_work_with_lower_case[char_index]

        if alphabet.__contains__(char_tested):
            index_in_alphabet = alphabet.index(char_tested)

            if chosen_action == "encode":
                new_index = index_in_alphabet + shift_number
            elif chosen_action == "decode":
                new_index = index_in_alphabet - shift_number
            else:
                print("Sorry! Something went wrong!")
                break

            while new_index < 0:
                new_index += len(alphabet)
            while new_index > (len(alphabet) - 1):
                new_index -= len(alphabet)

            crypto_text += alphabet[new_index]
        else:
            crypto_text += char_tested

    print(f"The {chosen_action}d text is: {crypto_text}\n")


def choice():
    print("What would you like to do | now?")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, "
                      "type 'q' to quit:\n").lower()

    if direction == "q":
        print("Thanks for trying out Caesar Cipher! Have a great day! Goodbye!")

    elif direction == "encode" or direction == "decode":
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))

        caesar_cipher(direction, text, shift)
        choice()

    else:
        print("Oops, you entered something unexpected!\n")
        choice()


choice()

