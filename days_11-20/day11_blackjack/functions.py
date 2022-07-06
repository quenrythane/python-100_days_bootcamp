from day11_blackjack import deck, player_money, play_deck, player_cards, computer_cards, bet
import random

def shuffle(deck_name):
    random.shuffle(deck_name)

def new_shuffled_deck():
    global deck
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
    global player_money
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
    global bet
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



