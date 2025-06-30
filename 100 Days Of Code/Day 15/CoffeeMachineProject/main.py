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
            print('\nEnjoy your Espresso!')   
        else:
            print("\nSorry. We don't have enough supplies.")
    
    report()

def latte(type_coffee, supplies):
    def report():
        if type_coffee == 'latte' and supplies['water'] >= 100 and supplies['milk'] >= 100 and supplies['coffee'] >= 25:    
            supplies['water'] -= 100
            supplies['milk'] -= 100
            supplies['coffee'] -= 25
            print('\nEnjoy your Latte!')
        else:
            print("\nSorry. We don't have enough supplies.")
            
    report()

def capuccino(type_coffee, supplies):
    def report():
        if type_coffee == 'capuccino' and supplies['water'] >= 100 and supplies['milk'] >= 200 and supplies['coffee'] >= 25:
            supplies['water'] -= 100
            supplies['milk'] -= 200
            supplies['coffee'] -= 25
            print("\nEnjoy your Capuccino!")
        else:
            print("\nSorry. We don't have enough supplies.")
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
        quarters = int(input('Put yours quarters. ')) * 0.2
        dime = int(input('Put yours dimes. ')) * 0.1
        nickel = int(input('Put yours nickels. ')) * 0.05
        penny = int(input('Put yours cents. ')) * 0.01
        total_coins = penny + nickel + dime + quarters

        if type_coffee == 'espresso' and total_coins >= 1.5:
            espresso(type_coffee, supplies)
        elif type_coffee == 'latte' and total_coins >= 2.5:
            latte(type_coffee, supplies)
        elif type_coffee == 'capuccino' and total_coins >= 3:
            capuccino(type_coffee, supplies)
        elif type_coffee == 'report':
            report()
        elif type_coffee == 'off':
            print('Bye! Have a good coffee.')
            machine = False
        else:
            print('Invalid option or insufficient money.')

decision()
