import random

# Para comentar o código é CRTL + K e descomentar é CRTL + U.

lista = ['arroz', 'batata']
resposta = random.choice(lista)
under = ''

print(resposta) 

tamanhopalavra = len(resposta)

for i in range(tamanhopalavra):
    under += '_' 

print(under)

vidas = 5
gameover = False
letras_certas = []

while not gameover:
    tentativa = input('Digite uma letra.\n').lower()
    
    display = ''
    
    for letra in resposta:
        if letra == tentativa:
            display += letra
            letras_certas.append(tentativa)
        elif letra in letras_certas:
            display += letra
        else:
            display += '_'
    
    if tentativa not in letras_certas and tentativa not in resposta:
        vidas -= 1

    print(display)
    print(f'Vidas restantes: {vidas}')

    if '_' not in display:
        gameover = True
        print('Você ganhou.')
    if vidas == 0:
        gameover = True
        print('Você perdeu.')
            





