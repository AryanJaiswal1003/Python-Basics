#Logical Operators [and, or, not]
# A and B [both conditions need to be true]
# A or B [only one condition need to be true]
# not A [the condition must be false]
#let say if a = 15
#Generally if we code a < 13 (it is incorrect or False)
#but when we code: not a < 13 (output is true, since 'a' is not less than 13)

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55: #Shortened version = elif 45 <= age <= 55:
        print("Everything is going to be OK. Have a Free Ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    if age >= 45 and age <= 55 and wants_photo == "Y":
        bill = 0

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")