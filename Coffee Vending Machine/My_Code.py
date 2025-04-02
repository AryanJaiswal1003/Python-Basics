# TODO 2: Resource Checking & Printing & Checking its sufficiency
# TODO 3: Processing Coins & Checking Transaction & Refunding in case of excess or unavailable of resources

from menu import options , resources
from logo import image
print(image)

def calculate_money(expense):
    print("Please Insert Coins.")
    quarters = int(input("How Many Quarters? "))
    dimes = int(input("How Many Dimes? "))
    nickles = int(input("How Many Nickles? "))
    pennies = int(input("How Many Pennies? "))
    user_money_sum = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if user_money_sum > expense:
        refund = user_money_sum - expense
        return f"Refund = $ {round(refund , 2)}."
    elif user_money_sum == expense:
        return f"Refund = $ 0.0"
    else:
        return f"Sorry that's not Enough Money. Money Refunded: $ {user_money_sum}."


#TODO 1: Asking out user for their preferences (espresso / latte / cappuccino)
game_over = False
w_con , c_con , m_con , value = 0 , 0 , 0 , 0

while not game_over:
    print("\n")

    user_input = input("What would you like to have? (Espresso/Latte/Cappuccino): ").lower()
    w_left = resources['water'] - w_con
    c_left = resources['coffee'] - c_con
    m_left = resources['milk'] - m_con

    if user_input == "report":
        print(f"Water: {w_left}ml\nMilk: {m_left}ml\nCoffee: {c_left}g\nMoney: $ {value}")
    else:
        if user_input == "espresso":
            if w_left < 50 or c_left < 20:
                print("Sorry there is Not Enough Water")
            else:
                w_con += options['espresso']['ingredients']['water']
                c_con += options['espresso']['ingredients']['coffee']
                value += options['espresso']['cost']
                print(calculate_money(options['espresso']['cost']))
                print("Here is your Espresso ☕️. Enjoy!")
        elif user_input == "latte":
            if w_left < 200 or m_left < 150 or c_left < 30:
                print("Sorry there is Not Enough Water & Milk")
            else:
                w_con += options['latte']['ingredients']['water']
                c_con += options['latte']['ingredients']['coffee']
                m_con += options['latte']['ingredients']['milk']
                value += options['latte']['cost']
                print(calculate_money(options['latte']['cost']))
                print("Here is your Latte ☕️. Enjoy!")
        elif user_input == "cappuccino":
            if w_left < 250 or m_left < 100 or c_left < 30:
                print("Sorry there is Not Enough Water & Milk")
            else:
                w_con += options['cappuccino']['ingredients']['water']
                c_con += options['cappuccino']['ingredients']['coffee']
                m_con += options['cappuccino']['ingredients']['milk']
                value += options['cappuccino']['cost']
                print(calculate_money(options['cappuccino']['cost']))
                print("Here is your Cappuccino ☕️. Enjoy!")
        elif user_input == "off":
            game_over = True
