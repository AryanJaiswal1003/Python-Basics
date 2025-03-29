print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
Bill = 0

#todo = work out how much they need to pay based on their choice.
if size =="S":
    Bill += 15
elif size == "M":
    Bill += 20
elif size == "L":
    Bill += 25
else:
    print("You have typed the wrong inputs.")

#todo: work out how much to add to their bill based on pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        Bill += 2
    else:
        Bill += 3

#todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    Bill += 1

print(f"Your final bill is: ${Bill}.")

"""My Version"""
# if size == "S":
#     Bill += 15
#     print("Cost of Small Size Pizza: $ 15")
#     if pepperoni == "Y":
#         Bill += 2
#         print("Pepperoni for Small Size Pizza: $ 2")
# if size == "M":
#     Bill += 20
#     print("Cost of Medium Size Pizza: $ 20")
#     if pepperoni == "Y":
#         Bill += 3
#         print("Pepperoni for Medium Size Pizza: $ 3")
# else:
#     Bill += 25
#     if pepperoni == "Y":
#         Bill += 3
#         print("Pepperoni for Large Size Pizza: $ 3")
#     if extra_cheese == "Y":
#         Bill += 1
#         print("Extra Cheese: $ 1")
#     print(f"Your Final Bill is: $ {Bill}")