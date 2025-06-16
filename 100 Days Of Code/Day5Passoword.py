import random

letra = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
simb = ['*', '/', '!', '@', '.']

senha = ''
senha_lista = []

print('////  Gerador de senhas  \\\\')

let = int(input('Quantas letras você deseja?\n'))
num = int(input('Quantos números você deseja?\n'))
sim = int(input('Quantos símbolos você deseja?\n'))

# Senha fraca 
for letras in range(0, let):
    senha += random.choice(letra)

for letras in range(0, num):
    senha += random.choice(numeros)

for letras in range(0, sim):
    senha += random.choice(simb)

print(f'\nEssa senha NÃO está embaralhada. Ela está na sequência que foi dado as ordens.  {senha}\n')

# Senha forte

for letras in range(0, let):
    senha_lista += random.choice(letra)

for letras in range(0, num):
    senha_lista += random.choice(numeros)

for letras in range(0, sim):
    senha_lista += random. choice(simb)

random.shuffle(senha_lista)
senha_lista = ''.join(senha_lista)   # Isso aqui converte a lista para string.

print(f'\nEssa senha ESTÁ embaralhada.   {senha_lista}\n')
