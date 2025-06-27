from art import *
Art = text2art('AUCTION')
print(Art)

pessoas = {}
todos_jogaram = True

def maior_valor(dicionario):
    vencedor = ''
    maior_aposta = 0
    for aposta in dicionario:
        total_aposta = dicionario[aposta]
        if total_aposta > maior_aposta:
            maior_aposta = total_aposta
            vencedor = aposta

    print(f'O vendedor é {vencedor} com a aposta de {maior_aposta}.')

while todos_jogaram:

    quem = str(input('Qual o nome de quem vai jogar?\n').lower())
    quanto = int(input('Quanto?\n'))
    outro = str(input('Mais alguém vai jogar? S ou N. \n').lower())
    pessoas[quem] = quanto

    if outro == 'n':
        todos_jogaram = False
        maior_valor(pessoas)
    else:
        print('\n' * 50)

 # Uma outra forma de pegar o valor máximo é com: 
 # max(pessoas, key=pessoas.get). Só vai retornar a pessoa. O valor, não.
