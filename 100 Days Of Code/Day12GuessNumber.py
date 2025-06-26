def GuessNumber():
    
    import random
    from art import tprint
    tprint('Guess  the  Number')

    RANDOM_NUMBER = random.randint(1, 10)
    
    print('You have to discover the number between 1 and 100.\n')

    def easy():
        LIVES = 10
        PLAYNG = True
        
        while PLAYNG:
            pick_numb = int(input(f'Pick a number. You have more {LIVES} attempts.\n'))

            if pick_numb == RANDOM_NUMBER:
                print('Good job!')
                PLAYNG = False
            else:
                LIVES -= 1
            
            if pick_numb > RANDOM_NUMBER:
                print('Too high!')
            elif pick_numb < RANDOM_NUMBER:
                print('Too low!')
            else:
                print('You guess the number!')

            if LIVES == 0:
                PLAYNG = False
                print(f'You lose! The right was {RANDOM_NUMBER}')


    def hard():
        
        LIVES = 5
        PLAYNG = True
        
        while PLAYNG:
            pick_numb = int(input(f'Pick a number. You have more {LIVES} attempts.\n'))

            if pick_numb == RANDOM_NUMBER:
                print('Good job!')
                PLAYNG = False
            else:
                LIVES -= 1
            
            if pick_numb > RANDOM_NUMBER:
                print('Too high!')
            elif pick_numb < RANDOM_NUMBER:
                print('Too low!')
            else:
                print('You guess the number!')

            if LIVES == 0:
                PLAYNG = False
                print(f'You lose! The right was {RANDOM_NUMBER}')

    print('Welcome to the Guess the number game!')
    level = input("\nChoose a difficulty. Type 'easy' or 'hard'. \n").lower()


    if level == 'easy':
        easy()
    elif level == 'hard':
        hard()
    else:
        print('Invalid option.')

GuessNumber()