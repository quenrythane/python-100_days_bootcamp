import random
# from functions import *

deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4

def shuffle(deck_name):
    random.shuffle(deck_name)

def new_shuffled_deck():
    play_deck = deck.copy()
    random.shuffle(play_deck)
    return play_deck

def deal_card():
    return play_deck.pop()

def show_playrer_hand():
    print(f"Your cards are: {' '.join(player_cards)}")

def show_computer_hand():
    if len(computer_cards) == 2:
        print(f"Croupiere cards are: {computer_cards[0]} _")
    else:
        print(f"Croupiere cards are: {' '.join(computer_cards)}")

def win(c_bet):
    print(f"You win ${c_bet}!")
    player_money += c_bet

def insurance():
    action = input("do you want to take insurance (y/n?): ").lower()
    if action == "n":
        pass
    elif action == "y":
        player_money -= 0.5 * bet
        print("You have taken insurence")
        if computer_cards[1] == "A":
            print("You win insurance!")
            player_money += bet
        else:
            print("You lost insurence")
    else:
        print("Wrong input. Try again")
        insurance()

def double_down():
    do_double_down = input("Do you want to double down? (y/n): ").lower()
    if do_double_down == "y":
        player_money -= bet
        bet *= 2
        player_cards.append(deal_card())
        return True
    elif do_double_down == "n":
        return False
    else:
        print("Wrong input. Try again")
        double_down()



def count_score(cards):
    score = 0
    for card in cards:
        if card == "A":
            score += 11
        elif card == "J" or card == "Q" or card == "K":
            score += 10
        else:
            score += int(card)
    if score > 21:
        if "A" in cards:
            score -= 10
    return score

def computer_drawing():
    if count_score(computer_cards) > 16:
        return count_score(computer_cards)
    else:
        computer_cards.append(deal_card())
        computer_drawing()



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


