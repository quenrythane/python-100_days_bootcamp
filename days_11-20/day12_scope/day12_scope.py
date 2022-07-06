# example 1
def create_enemies():
    enemies = ['cat', 'dog', 'elephant']
    return enemies


create_enemies()
new_enemy = enemies[0]  # error because of scope (behind correct scenario)
print(new_enemy)


# example 2
def create_enemies2():
    global enemies2
    enemies2 = ['cat', 'dog', 'elephant']
    return enemies2


create_enemies2()
new_enemy2 = enemies2[0]
print(new_enemy2)
