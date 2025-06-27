# Variáveis globais devem ser escritas em maiúsculo. Isso agiliza na hora de ler e interpretar o código.

# Global Scope
ENEMIES = 1

# Local Scope
def incrise_enemies():
    enemies = 2
    print(f'Enemies insede the function {enemies}')

incrise_enemies()
print(enemies)

# Global Scope
PLAYER_HEALTH = 10

# Local Scope
def game():
    def drink_potion():
        potion = 2
        print(player_healt)
    
    drink_potion()

game()
print(potion) # Da erro porque ela só pode ser acessa se chamar a função Game toda. Ela não é de escopo global.

# # O python não tem Block Scope

# Vericica se o número é primo
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Verifica se o número é primo usando raiz quadrada. É melhor para grandes números.
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

What will be printed in the console when the following code is run?

DO NOT run the code, just pretend to be a computer.

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
print(a_variable)

R = NameError

What will be printed in the console when the code is run?

DO NOT run the code, just pretend to be a computer.

i = 50
def foo():
    i = 100
    return i
 
foo()
print(i)

R = 50

What will be printed in the console when the following code is run?

DO NOT run the code, just pretend to be a computer.

def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()

R = 16

# Criar uma lista de 1 a 100
numbers = list(range(1, 101))
print(numbers)
