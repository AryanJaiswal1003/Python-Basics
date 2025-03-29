print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    .--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .  `` ,  `"-._"-._   ". '|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,.--o;   |
|___________________|_| ;     (#) -.o "=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?" )
direction = input("Type 'left' or 'right'\n").lower()
if direction == "left": #or direction == "Left" [if we don't use 'lower()']
    print("You've come to a Lake. There is an island in the Middle of the Lake.")
    Action = input('''Type "wait" to Wait a Boat. Type "swim" to Swim across.\n''').lower()
    if Action == "wait":
        print("You have arrived at the island unharmed. There is a House with 3 Doors.")
        Doors = input('''  One red, one yellow and one blue. Which colour do you choose?\n ''').lower()
        if Doors == "red":
            print("It's a Room full of Fire. Game over & Try again.")
        elif Doors == "blue":
            print("It's a Room full of Venomous Snakes. Game over & Try again.")
        elif Doors == "yellow":
            print("You find the Treasure!! You Win")
        else:
            print("You chose a Door that doesn't exist. Game over & Try again.")
    else:
        print("You got Attacked by Hungry Crocodiles. Game over & Try again.")

else:
    print("You fell into a Hole. Game over & Try again.")
