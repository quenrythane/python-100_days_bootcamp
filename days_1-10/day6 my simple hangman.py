import random

lifes = 5
words = ["tata", "mama", "wujek", "kot", "pies", "krowa", "kotek", "kaczka", "kotka", "kotek"]
chosen_word = random.choice(words)
display = "-" * len(chosen_word)

print("elo gramy")
print(display)

while lifes:
    if display == chosen_word:
        print("You win!")
        break

    print(f"You have {lifes} lives left.")
    guess = input("Zgadnij literę: ").lower()
    if guess not in chosen_word:
        print("Nie ma takiej litery")
        lifes -= 1


    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display = display[:index] + letter + display[index + 1:]
    print(display, "\n")

if lifes == 0:
    print("You lose!")