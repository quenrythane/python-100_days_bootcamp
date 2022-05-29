while True
    # player turn
    player_total = 0
    for card in player_cards:
        if card == "A":
            player_total += 11
        elif card == "J" or card == "Q" or card == "K":
            player_total += 10
        else:
            player_total += int(card)

    # check if player has 21
    if player_total == 21:
        print("You win!")
        break

    # check if player has busted
    elif player_total > 21:
        print("You busted!")
        break

    # if player has not busted, ask player if he wants to hit or stand
    else:
        hit_or_stand = input("Hit or Stand? Enter 'h' or 's' ")
        if hit_or_stand == "h":
            # player hits
            player_cards.append(play_deck.pop())
            print("Your cards are: ")
            for card in player_cards:
                print(card)
            print("Your total is: " + str(player_total))
        elif hit_or_stand == "s":
            # player stands
            print("Your cards are: ")
            for card in player_cards:
                print(card)
            print("Your total is: " + str(player_total))

            # computer turn
            computer_total = 0
            for card in computer_cards:
                if card == "A":
                    computer_total += 11
                elif card == "J" or card == "Q" or card == "K":
                    computer_total += 10
                else:
                    computer_total += int(card)

            # check if computer has busted
            if computer_total > 21:
                print("Computer busted!")
            # check if computer has 21
            elif computer_total == 21:
                print("Computer wins!")
            # if computer has not busted or 21, ask computer if he wants to hit or stand
            else:
                while computer_total < 17:
                    computer_cards.append(play_deck.pop())
                    computer_total = 0
                    for



print(player_cards)
print(computer_cards)

