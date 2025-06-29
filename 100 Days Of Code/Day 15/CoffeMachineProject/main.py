from art import tprint
tprint('Coffee   Machine')

type_coffee = input("What would you like? (espresso/latte/cappuccino)  ")

supplies = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

def report():
    print(supplies['water'],'\n',
          supplies['milk'], '\n',
          supplies['coffee'], '\n',
          supplies['money'])

def espresso(type_coffee, supplies): 
    def report():
        if type_coffee == 'espresso' and supplies['water'] >= 100 and supplies['coffee'] >= 15:
            supplies['water'] -= 100
            supplies['coffee'] -= 15
            print('Enjoy your Espresso!')   
        else:
            print("Sorry. We don't have enough supplies.")
    
    report()

def latte(type_coffee, supllies):
    def report():
        if type_coffee == 'latte'and supplies['water'] >= 100 and supplies['milk'] >= 100 and supplies['coffee'] <= 25:    
            supplies['water'] -= 100
            supplies['milk'] -= 100
            supplies['coffee'] -= 25
            print('Enjoy your Latte!')
        else:
            print( "Sorry. We don't have enough supplies.")
            
    report()

def capuccino(type_coffee, supllies):
    def report():
        if type_coffee == 'capuccino'and supplies['water'] >= 100 and supplies['milk'] >=200 and supplies['coffee'] <= 25:
            supplies['water'] -= 100
            supplies['milk'] -= 200
            supplies['coffee'] -= 25
            print("Enjoy your Capuccino!")
        else:
            print( "Sorry. We don't have enough supplies.")
    report()

def decision():
    machine = True
    while machine:
        type_coffee = input("What would you like? (espresso/latte/cappuccino)  ")
        
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