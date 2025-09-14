import random


level_easy = 10
level_hard = 5

def choose_and_check(user_guess, actual_answer, turns):
    if user_guess == actual_answer:
        print("You've got it, congrats")

        
        
    elif user_guess > actual_answer:
        print('Too high')
        return turns - 1
    else:
        print('Too low')
        return turns - 1


def set_difficulty():
    level_difficulty = input("Choose a level dificulty 'easy' or 'hard': ")

    if level_difficulty == "easy":
        return level_easy
    else:
        return level_hard

def game():
    attemp_turns = set_difficulty()
    user_guess = 0
    answer = random.randint(1, 100)
    print(answer)
    print("Guess my number between 1 to 100\nI'm thinking in a number, what's it?'")

    while user_guess != answer:
        if attemp_turns > 0:
            user_guess = int(input("Guess a number: "))
            attemp_turns = choose_and_check(user_guess=user_guess, actual_answer=answer, turns=attemp_turns)
            print(attemp_turns)
        else:
            print(f'Nah, the correct answer was {answer}')
            break
game()