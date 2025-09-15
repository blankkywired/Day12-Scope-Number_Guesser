import random

LEVEL_EASY = 10
LEVEL_HARD = 5

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
        return LEVEL_EASY
    else:
        return LEVEL_HARD
def game():
    attemp_turns = set_difficulty()
    user_guess = 0
    answer = random.randint(1, 100)
   #print(answer)
    print("Guess my number between 1 to 100\nI'm thinking in a number, what's it?'")

    while user_guess != answer:
        if attemp_turns > 0:
            user_guess = int(input("Guess a number: "))
            attemp_turns = choose_and_check(user_guess=user_guess, actual_answer=answer, turns=attemp_turns)
            print(f'Attempts left:{attemp_turns}')
        else:
            print(f'Nah, the correct answer was {answer}')
            break
game()

#DFluxograma

#1 - a funçao game() inicia o codigo, o usuario escolhe o nivel de dificuldade
#2 - A dificuldade encrementa o numero maximo de tentativas que o usuario terá ate acertar o numero
#3 - A resposta é escolhida pelo modulo random.randint
#4 - A função check a cada iteração do usuario ira checar o numero do usuario,a resposta escolhida inicialmente  e a quantidade de tentativas restantes
#5 - aa variavel attemp_turns recebe o valor de dentro de uma função(set_difficulty), e tambem será usada como parametro dentro da função check, e a cada erro do usuario será subtraido uma unidade