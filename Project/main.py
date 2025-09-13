from random import randint

computer_guess = randint(0, 100)

choice_difficulty = input("Choose a difficulty level: 'easy' or 'hard':" ).lower()

if choice_difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

first_choice = int(input('Make a guess:'))
start = True
while start:
    if attempts > 0:
        if first_choice == computer_guess:
            print("Congrats, you've get it")
            break
        
        elif first_choice > computer_guess:
            print('Too high')
            first_choice = int(input('Make a guess:'))
            attempts -= 1
            print(f'Attempts left: {attempts}')

        elif first_choice < computer_guess:
            print('Too low')
            first_choice = int(input('Make a guess:'))
            attempts -= 1
            print(f'Attempts left: {attempts}')
    else:
        print('You lose')
        break
    


        
        
    