from art import tprint

tprint('Coffee   Machine')

supplies = {
    'water': 300,
    'milk': 200,
    'coffee': 75,
    'money': 0
}

def espresso(type_coffee, supplies): 
    def report():
        if type_coffee == 'espresso' and supplies['water'] >= 100 and supplies['coffee'] >= 15:
            supplies['water'] -= 100
            supplies['coffee'] -= 15
            print('Enjoy your Espresso!')   
        else:
            print("Sorry. We don't have enough supplies.")
    
    report()

def latte(type_coffee, supplies):
    def report():
        if type_coffee == 'latte' and supplies['water'] >= 100 and supplies['milk'] >= 100 and supplies['coffee'] >= 25:    
            supplies['water'] -= 100
            supplies['milk'] -= 100
            supplies['coffee'] -= 25
            print('Enjoy your Latte!')
        else:
            print("Sorry. We don't have enough supplies.")
            
    report()

def capuccino(type_coffee, supplies):
    def report():
        if type_coffee == 'capuccino' and supplies['water'] >= 100 and supplies['milk'] >= 200 and supplies['coffee'] >= 25:
            supplies['water'] -= 100
            supplies['milk'] -= 200
            supplies['coffee'] -= 25
            print("Enjoy your Capuccino!")
        else:
            print("Sorry. We don't have enough supplies.")
    report()

def report():
    print("\nCurrent Supplies:")
    print("Water:", supplies['water'])
    print("Milk:", supplies['milk'])
    print("Coffee:", supplies['coffee'])
    print("Money:", supplies['money'])

def decision():
    machine = True
    while machine:
        type_coffee = input("\nWhat would you like? (espresso/latte/capuccino): ").lower()
        
        if type_coffee == 'espresso':
            espresso(type_coffee, supplies)
        elif type_coffee == 'latte':
            latte(type_coffee, supplies)
        elif type_coffee == 'capuccino':
            capuccino(type_coffee, supplies)
        elif type_coffee == 'report':
            report()
        elif type_coffee == 'off':
            print('Bye! Have a good coffee.')
            machine = False
        else:
            print('Invalid option.')

decision()
