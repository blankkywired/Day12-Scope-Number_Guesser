
JhonAge = 27
def calc_new_age():
    JhonAge = 30
    print(JhonAge)

calc_new_age() # --> Return Jhon's age inside the function Output: 30
print(JhonAge) # --> Return the initial Jhon's age outside the function Output: 27


game_level = 3
enemy = ["Skeleton", "Zombie", "Witch"]
def create_new_enemy():
    if game_level < 5:
        new_enemy = enemy[0]
    print(new_enemy)
create_new_enemy()
print(new_enemy) # --> Don't show any value because the variable value its inside the function, return NameError, is not defined