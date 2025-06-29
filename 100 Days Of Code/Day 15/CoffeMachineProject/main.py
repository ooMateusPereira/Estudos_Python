from art import tprint
tprint('Coffee   Machine')

machine = True
type_coffee = input("What would you like? (espresso/latte/cappuccino)  ")

supplies = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

def decision():
    if type_coffee == 'espresso':
        supplies['water'] -= 100
        supplies['coffe'] -= 15
    elif type_coffee == 'latte':
        supplies['water'] -= 100
        supplies['milk'] -= 100
        supplies['coffee'] -= 25
    elif type_coffee == 'capuccino':
        supplies['water'] -= 100
        supplies['milk'] -= 200
        supplies['coffee'] -= 25
    elif type_coffee == 'report':
        print(f"Wather:", supplies['water'],
            '\nMilk:  ', supplies['milk'], 
            '\nCoffee:', supplies['coffee'], 
            '\nMoney:', '$', supplies['money'])
    elif type_coffee == 'off':
        print('Bye! Have a good coffee.')
        machine = False

def check_supplies():
    