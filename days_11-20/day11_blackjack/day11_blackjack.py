from functions import *

deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4


# start game
# init game
playing = True
player_money = 100
play_deck = new_shuffled_deck()

while playing and player_money > 0:
    # check if we have enough card in play_deck
    if len(play_deck) < 10:
        play_deck = new_shuffled_deck()

    # take bet
    print("You have $" + str(player_money))
    bet = 10  # int(input("How much do you want to bet?: "))
    player_money -= bet

    # init player and computer cards
    player_points = 0
    computer_points = 0
    player_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    show_playrer_hand()
    show_computer_hand()




    if computer_cards[0] == "A":
        insurance()
    while True:
        if len(player_cards) == 2:
            if double_down():
                player_points = count_score(player_cards)
                if player_points > 21:
                    print("You lost!")
                    break
                elif player_points == 21:
                    win(bet * 2.5)
                    break
                else:
                    computer_points = computer_drawing()


