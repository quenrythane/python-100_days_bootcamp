from data import *
from machine_functions import *

money = 10
print(money)

# init
want_order = "y"

# program
while want_order != "n":
    want_order = input("Welcome to the coffee machine! Do you want to order coffee? (y/n): ")
    if want_order == "n":
        break

    order = input(f"What do you want to order? ({'/'.join(x for x in MENU)}): ").lower()
    print()

    if order == "report":
        report()

    elif order == "add":
        add_resources()

    elif order in MENU:
        # check if enough resources
        if resources["water"] >= MENU[order]["ingredients"]["water"] \
                and resources["milk"] >= MENU[order]["ingredients"]["milk"]\
                and resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:

            # take payment
            print(f"{order} cost is ${MENU[order]['cost']}.", end=" ")
            amount = take_coins()

            # make coffee
            if amount >= MENU[order]["cost"]:
                resources["water"] -= MENU[order]["ingredients"]["water"]
                resources["milk"] -= MENU[order]["ingredients"]["milk"]
                resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
                money += MENU[order]["cost"]

                print(f"Here is your {order}")
                print(f"you paid ${amount} and cost was ${MENU[order]['cost']}.", end=" ")
                if amount > MENU[order]["cost"]:
                    print(f"Here is your change ${float('{0:.2f}'.format(amount - MENU[order]['cost']))}")
                print()

            else:
                print(f"Not enough money. Here is your money back ${amount}")

        # if not enough
        else:
            print(f"Sorry, not enough resources to make {order} :(")
    else:
        print(f"Sorry, we don't have {order} :(")
