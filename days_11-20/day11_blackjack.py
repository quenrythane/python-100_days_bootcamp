import random

list_of_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4


def shuffle():
    random.shuffle(list_of_cards)

shuffle()
print(list_of_cards)


player_cards = []
computer_cards = []
for card in list_of_cards:







