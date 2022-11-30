alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text_to_encrypt, shift_number):
    text_to_encrypt_lower_case = text_to_encrypt.lower()
    encrypted_text = ""

    for initial_char_index in range(0, len(text_to_encrypt_lower_case)):
        char_tested = text_to_encrypt_lower_case[initial_char_index]
        if alphabet.__contains__(char_tested):
            index_in_alphabet = alphabet.index(char_tested)
            # print(index_in_alphabet)
            new_index_after_shift = index_in_alphabet + shift_number
            # print(new_index_after_shift)
            while new_index_after_shift < 0:
                new_index_after_shift += len(alphabet)
            while new_index_after_shift > (len(alphabet) - 1):
                new_index_after_shift -= len(alphabet)
                # print(new_index_after_shift)
            encrypted_text += alphabet[new_index_after_shift]
        else:
            encrypted_text += char_tested

    print(f"The encoded text is: {encrypted_text}")


def decrypt(text_to_decrypt, shift_number):
    text_to_decrypt_lower_case = text_to_decrypt.lower()
    decrypted_text = ""

    for initial_char_index in range(0, len(text_to_decrypt_lower_case)):
        char_tested = text_to_decrypt_lower_case[initial_char_index]
        if alphabet.__contains__(char_tested):
            index_in_alphabet = alphabet.index(char_tested)
            # print(index_in_alphabet)
            new_index_after_re_shift = index_in_alphabet - shift_number
            # print(new_index_after_re_shift)

            while new_index_after_re_shift > (len(alphabet) - 1):
                new_index_after_re_shift -= len(alphabet)
                # print(new_index_after_re_shift)

            while new_index_after_re_shift < 0:
                new_index_after_re_shift += len(alphabet)
                # print(new_index_after_re_shift)

            decrypted_text += alphabet[new_index_after_re_shift]
        else:
            decrypted_text += char_tested

    print(f"The decoded text is: {decrypted_text}")


print("Hi! Welcome to Caesar Cipher!")
print("What would you like to do?")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction == "encode":
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
elif direction == "decode":
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    decrypt(text, shift)
else:
    print("Oops, you entered something unexpected!")


