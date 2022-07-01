score = 100

with open("score.txt", "r") as file:
    highscore = int(file.read())

if score > highscore:
    with open("score.txt", "w") as file:
        file.write(str(score))
