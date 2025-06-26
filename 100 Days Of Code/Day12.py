# Global Scope
enemies = 1

# Local Scope
def incrise_enemies():
    enemies = 2
    print(f'Enemies insede the function {enemies}')

incrise_enemies()
print(enemies)

# Global Scope
player_healt = 10

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