enemy = ["Whitch", "Zombie", "Skeleton"]

def add_new_enemy():
    global enemy
    enemy = "Enderman"
    print(enemy)

print(enemy) # --> imprime o valor anterior da lista
add_new_enemy() # --> cria uma variavel global enemy que atualiza o valor mesmo estando dentro de uma função

print(enemy) # --> agora imprime o novo valor mesmo apos ser incrementado dentro da função