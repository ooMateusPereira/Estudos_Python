from art import tprint
import random
tprint('Black Jack')
print('Welcome to Black Jack game!')

cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game = True

while game:

    player1 = random.choice(cards_list)
    player2 = random.choice(cards_list)
    print(f'That are your hand {player1}')
    


    print(player1, player2)
