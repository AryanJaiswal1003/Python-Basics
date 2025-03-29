letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!!!")
letter = int(input("How many letters you would like to have in your Password?\n"))
number = int(input("How many numbers would you like to have in your Password?\n"))
symbol = int(input("How many symbols would you like to have in Password?\n"))

#Easy Password Generator

# import random
# Password = ""
#
# for char in range(0 , letter):
#     Password += random.choice(letters)
# for char in range(0 , number):
#     Password += random.choice(numbers)
# for char in range(0 , symbol):
#     Password += random.choice(symbols)
#
# print(f"Your Password is: {Password}")

#Hard Password Generator

import random
Password = []

for char in range(0 , letter):
    Password += random.choice(letters) #Password.append(random.choice(letters))
for char in range(0 , number):
    Password += random.choice(numbers) #Password.append(random.choice(numbers))
for char in range(0 , symbol):
    Password += random.choice(symbols) #Password.append(random.choice(symbols))

print(Password)
random.shuffle(Password)
print(Password)

password = ""
for character in Password:
    password += character

print(f"Your Password is: {password}")