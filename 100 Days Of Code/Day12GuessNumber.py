import random
from winsound import PlaySound
from art import tprint
tprint('Guess  the  Number')

RANDOM_NUMBER = random.randint(1, 100)


def GuessNumber():

    print('You have 5 attempts to discover the number between 1 and 100.\n')

    def easy():
            LIVES = 5
            PLAYNG = True

            pick_numb = int(input('Pick a number\n'))
            while PLAYNG:
                if pick_numb == RANDOM_NUMBER:
                    print('Good job! You guess the number!')
                    PLAYNG = False
                else:
                    LIVES -= 1
                    pick_numb = int(input(f'Pick another number. You have more {LIVES} attempts.\n'))
                
                if pick_numb != RANDOM_NUMBER:
                    if LIVES == 0:
                        PLAYNG = False
                        print(f'You lose! The right was {RANDOM_NUMBER}')

                        
    def hard():
        print('You have 5 attempts')


    print('Welcome to the Guess the number game!')
    level = input("\nChoose a difficulty. Type 'easy' or 'hard'. \n").lower()


    if level == 'easy':
        easy()
    elif level == 'hard':
        hard()
    else:
        print('Invalid option.')

GuessNumber()