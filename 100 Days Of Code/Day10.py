# O return mostra ao computador a onde o código acaba. 
# É possível se ter vários dentro de uma função.

# Transformar a primeira letra em maiscúla e as outras em minúsculas. 
def format_name(first, last):
    first_1 = first.title()
    last_1 = last.title()

    return f'{first_1} {last_1}'

print(format_name('MATEUS','pereira'))

# Outra forma de fazer 
def format_name(first, last):
    first_1 = first.title()
    last_1 = last.title()

    return f'Resulto: {first_1} {last_1}'

print(format_name(input('Primeiro nome: \n'), input('Segundo nome: \n')))

# É possível usar uma função como paramêtro para outra.
def fun1(text, text1):
    return text + ' ' + text1

def fun2(text):
    return text.title()

output = fun2(fun1('MATEUS', 'PEreira'))

print(output)

# Caso o usuário não escreva
def format_name(first, last):
    if first_1 == '' or last_1 == '':
        return 'Erro.'

    first_1 = first.title()
    last_1 = last.title()

    return f'Resulto: {first_1} {last_1}'

print(format_name(input('Primeiro nome: \n'), input('Segundo nome: \n')))


What will be printed in the console after running the following code?

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

R = None

What would you predict to be the result of running the following code?

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

R = 15