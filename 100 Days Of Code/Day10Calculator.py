from art import tprint

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    tprint("CALCULATOR")

    active = True
    numb1 = float(input('Type the first number: \n'))

    while active:
        
        
        chose = str(input('Choose your operation. \n'
        '+\n' 
        '-\n' 
        '*\n' 
        '/\n'))                  
        numb2 = float(input('Type the second number: \n'))

        if chose in operations:
            result = operations[chose](numb1, numb2)
            print(f"The result of {numb1} {chose} {numb2} is: {result}")
        else:
            print("Invalid operation.")

        again = str(input('Do you want play again?\n' \
        'Type: ''Y'' or ''N''\n')).lower()
        
        if again == 'y':
            numb1 = result
        else:
            print('Thank you for use our app.')
            active = False
            
calculator()

# Desta forma está errado porque eu não estava salvado o resultado em lugar nenhum, logo, quando eu usava o PRINT aparecia o endereço na memória, não o resultado da operação.
# if chose == "+":
#     add(numb1, numb2)
#     print(add)

# if chose == "-":
#     subtract(numb1, numb2)
#     print(subtract)

# if chose == "*":
#     multiply(numb1, numb2)
#     print(multiply)

# if chose == "/":
#     divide(numb1, numb2)
#     print(divide)

