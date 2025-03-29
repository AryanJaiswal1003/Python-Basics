alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the Encoded Result: {cipher_text}")
#
# def decrypt(original_text , shift_amount): #jgnnq 'hello' shifted 2 positions
#     decipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         decipher_text += alphabet[shifted_position]
#     print(f"Here is the Decoded Result: {decipher_text}")
#
# def caesar(): #MY WAY - Uses the above created functions
#     if direction == 'encode':
#         encrypt(original_text=text, shift_amount=shift)
#     if direction == 'decode':
#         decrypt(original_text=text , shift_amount=shift)

def caesar(original_text, shift_amount, encode_or_decode): #No use of above created functions
    output = ""
    for letter in original_text:
        if encode_or_decode == 'encode':
            result = alphabet.index(letter) + shift_amount
            result %= len(alphabet)
            output += alphabet[result]
        if encode_or_decode == 'decode':
            result = alphabet.index(letter) - shift_amount
            result %= len(alphabet)
            output += alphabet[result]

    print(f"Your {encode_or_decode}d Result is = {output}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)