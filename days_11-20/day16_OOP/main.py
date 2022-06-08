from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# init
want_order = "y"
CoffeeMaker = CoffeeMaker()
MENU = Menu()
Money_Mach = MoneyMachine()


# program
want_order = "y"

while want_order != "n":
    want_order = input("Welcome to the coffee machine! Do you want to order coffee? (y/n): ")
    if want_order == "n":
        break

    order = input(f"What do you want to order? ({'/'.join(x for x in MENU.get_items().split())}): ").lower()
    print()

    if order == "report":
        CoffeeMaker.report()
        Money_Mach.report()
        print()

    elif order in MENU.get_items():
        drink = MENU.find_drink(order)
        if CoffeeMaker.is_resource_sufficient(drink):
            print(f"{order} cost is ${drink.cost}.")
            if Money_Mach.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)
                print()


