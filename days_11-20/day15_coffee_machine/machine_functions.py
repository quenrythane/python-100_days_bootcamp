from data import *


def report():
    for k, v in resources.items():
        if k == "coffee":
            print(f"{k}: {v}g")
        else:
            print(f"{k}: {v}ml")
    print(f"Money: ${money}\n")


def take_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    print()
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01


def add_resources():
    print("Please add resources")
    water = int(input("How much water?(ml): "))
    milk = int(input("How much milk?(ml): "))
    coffee = int(input("How much coffee?(g): "))
    print()
    resources["water"] += water
    resources["milk"] += milk
    resources["coffee"] += coffee


def add_money(amount):
    global money
    money += amount
