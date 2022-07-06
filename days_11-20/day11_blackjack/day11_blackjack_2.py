from blackjack_functions import *

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4


# init game
player_money = 100
play_deck = new_shuffled_deck(deck)

playing = 'y'
while playing == 'y':
    # check is card is enough
    if len(play_deck) < 10:
        play_deck = new_shuffled_deck(deck)

    # take bet
    print("You have $" + str(player_money))
    bet = 10  # float(input("How much do you want to bet? "))
    print("You bet is $" + str(bet) + '\n')
    player_money -= bet

    # give cards
    player_cards = [play_deck.pop() for _ in range(2)]
    computer_cards = [play_deck.pop() for _ in range(2)]

    # show cards
    print(show_player_hand(player_cards))
    print(show_computer_hand(computer_cards, False))

    # player turn
    action = "h"
    while action != "s":
        action = input("do you want to (h)it or (s)tand? ").lower()
        # stand
        if action == "s":
            print("You stand \n")
            break

        # hit
        elif action == "h":
            player_cards.append(play_deck.pop())
            # show cards
            print(show_player_hand(player_cards))
            print(show_computer_hand(computer_cards, False))

        # invalid input
        else:
            print("Invalid input!")
            continue

        # check player_points
        player_score = count_score(player_cards)
        if player_score > 21:
            print("You overload! \n")
            break

    # computer turn
    if count_score(player_cards) < 22:
        while count_score(computer_cards) < 17:
            computer_cards.append(play_deck.pop())
            print(show_computer_hand(computer_cards))

    # final result
    print(show_player_hand(player_cards))
    print(show_computer_hand(computer_cards))
    player_score = count_score(player_cards)
    computer_score = count_score(computer_cards)

    # player has 21
    if player_score == 21:
        if computer_score == 21:
            print("Draw...")
        else:
            player_money += bet * 2.5
            print(f"You win! {bet * 2.5}")

    # player has too much
    elif player_score > 21:
        print("You lost!")

    # computer has too much
    elif computer_score > 21:
        player_money += bet * 2
        print(f"You win ${bet*2}!")

    # you have more than computer_score (but no one have more than 21)
    elif player_score > computer_score:
        player_money += bet * 2
        print(f"You win ${bet * 2}!")

    # you lost
    else:
        print("You lost!")

    print(f"You have ${player_money} now!")

    playing = input("Do you want to play again? (y/n) ").lower()
    while playing not in ['y', 'n']:
        playing = input("You misspell. Do you want to play again? (y/n) ").lower()

