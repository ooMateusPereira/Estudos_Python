import random

letras = ['A', 'a', 'B', 'b', 'C', 'c']
numeros = ['1', '2', '3', '4']
simbolos = ['!', '@', '#']

senha = []

let = int(input('Quantas letras?\n'))
num = int(input('Quantos números?\n'))
sim = int(input('Quantos símbolos?\n'))

for n in range(0, let):
    senha += random.choice(letras)

for n in range(0, num):
    senha += random.choice(numeros)

for n in range(0, sim):
    senha += random.choice(simbolos)

random.shuffle(senha)

senha = ''.join(senha)

print(senha)