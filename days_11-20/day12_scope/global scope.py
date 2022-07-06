def create_enemies():
    global enemies
    enemies = ['cat', 'dog', 'elephant']
    return enemies


enemies = []
create_enemies()

new_enemy = enemies[0]
print(new_enemy)