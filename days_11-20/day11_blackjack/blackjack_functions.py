import random

def new_shuffled_deck(deck):
    play_deck = deck.copy()
    random.shuffle(play_deck)
    return play_deck

def show_player_hand(player_cards):
    return f"Your cards are: {' '.join(player_cards)}. Current score: {count_score(player_cards)}"

def show_computer_hand(computer_cards, show_all=True):
    if show_all:
        return f"Croupier cards are: {' '.join(computer_cards)}. Current score: {count_score(computer_cards)}"
    else:
        return f"Croupier cards are: {computer_cards[0]} _. Current score: {count_score(computer_cards[0])}"

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

