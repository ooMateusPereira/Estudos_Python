# Algortimo para ver qual é o maior número da lista
numeros = (100, 111, 150, 230, 555, 1020, 1555, 99)
maximo = 0

for maior in numeros:
   if maior > maximo:
        maximo = maior
print(maximo)


# Somador de números estilo Gauls
total = 0

for number in range(1, 101):
    total += number
print(total)

# Deixar o print antes do input vai gerar erro na hora de armazenar e interpretar a função

let = int(input('Quantas letras você deseja?'))    # CERTO

let = print(int(input('Quantas letras você deseja?')))   # ERRADO

# O random.shuffle() só funciona com LISTAS.