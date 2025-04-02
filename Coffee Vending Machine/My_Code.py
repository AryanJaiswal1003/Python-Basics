#TODO 2: Resource Checking & Printing & Checking its sufficiency
#TODO 3: Processing Coins & Checking Transaction & Refunding in case of excess or unavailablity of resources

from menu import options , resources

"""Resource Checking"""
def resources():
    water = resources['water']
    coffee = resources['coffee']
    milk = resources['milk']
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g")

resources()
#TODO 1: Asking out user for their preferences (espresso / latte / cappucchino)
user_input = input("What would you like to have? (Espresso/Latte/Cappuccino): ").lower()