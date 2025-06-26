# from art import tprint
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


# Professor's code

import random
from art import tprint

def deal_card():
    '''Returns a random card from the deck.'''

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choice(cards)
    return cards

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return 'Draw.'
    elif c_score == 0:
        return 'Lose, opponet has BlackJack.'
    elif u_score == 0:
        return 'Win with a BlackJack.'
    elif u_score > 21:
        return 'You went over. You lose.'
    elif c_score > 21:
        return 'Opponet went over. You win.'
    elif u_score > c_score:
        return 'You win.'
    else:
        return 'You lose'

def play_game():
    tprint('Black Jack')
    
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or type 'n' to pass: \n").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_score}, final score: {user_score}\n")
    print(f"\nComputer's final hand: {computer_cards}, final score: {computer_score}\n")
    print(compare(user_score, computer_score))

print('\n' * 50)
while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    play_game()