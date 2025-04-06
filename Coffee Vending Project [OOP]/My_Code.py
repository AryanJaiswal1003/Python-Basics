
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    choice = input(f"What would you like to have? [{menu.get_items()}]: ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink_choice = menu.find_drink(order_name=choice)
        if coffee_maker.is_resource_sufficient(drink=drink_choice):
            if money_machine.make_payment(cost=drink_choice.cost):
                coffee_maker.make_coffee(order=drink_choice)

