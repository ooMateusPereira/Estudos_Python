from art import tprint
# import random
# tprint('Black Jack')
# print('Welcome to Black Jack game!\n')

# cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# player1 = []
# player2 = []

# player1.append(random.choice(cards_list))
# player2.append(random.choice(cards_list))
# print(f'That are your hand: {player1}\n')

# game = True
# while game:

#     another_card = input('Type ''A'' to get another card.\n').lower()

#     if another_card == 'a':
#         player1.append(random.choice(cards_list))
#         player2.append(random.choice(cards_list))
#         print(f'\nThat are your hand: {player1}\n')
#         print(f'\nThat are your opponents hands: {player2}\n')

#         total_player1 = sum(player1)
#         total_player2 = sum(player2)

#         if total_player1 > 21:
#             print('You lost! You went over 21.\n')
#             print(f'Your opponent has {total_player2} and you have {total_player1}.')
#             game = False
#         elif total_player2 > 21:
#             print('You win! Your opponent went over 21.\n')
#             print(f'Your opponent has {total_player2} and you have {total_player1}.')
#             game = False
#         elif total_player1 > total_player2:
#             print('You win!\n')
#             print(f'Your opponent has {total_player2} and you have {total_player1}.')
#             game = False
#         elif total_player2 > total_player1:
#             print('You lost!\n')
#             print(f'Your opponent has {total_player2} and you have {total_player1}.')
#             game = False
#         else:
#             print('Draw!\n')
#             print(f'Your opponent has {total_player2} and you have {total_player1}.')
#             game = False
#     else:
#         print('Invalid character. Restart the game.')
#         game = False
