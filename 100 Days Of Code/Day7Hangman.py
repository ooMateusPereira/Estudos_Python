import random

from art import *
Art = text2art('HANGMAN')
print(Art)

palavras = ['maria', 'balao', 'mamao']

palavra = random.choice(palavras)  
corretas = []
#placeholder = '_' * len(palavra)
game_over = False
vidas = 5

while not game_over:
    tentativa = input('Digite uma letra\n').lower()
    
    display = ''

    for letra in palavra:
        if letra == tentativa:
            display += letra
            corretas.append(tentativa)
        elif letra in corretas:
            display += letra
        else:
            display += '_'

    print(display)

    if tentativa not in palavra and tentativa not in corretas:
        vidas -= 1
        print(f'Você ainda tem {vidas} vidas.')
        if vidas == 0:
            game_over = True
            print('Você perdeu.')

    if '_' not in display:
        game_over = True
        print('Você venceu.')
