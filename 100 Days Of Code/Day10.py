# Transformar a primeira letra em maiscúla e as outras em minúsculas. 
def format_name(first, last):
    first_1 = first.title()
    last_1 = last.title()

    return f'{first_1} {last_1}'

print(format_name('MATEUS','pereira'))


# É possível usar uma função como paramêtro para outra.
def fun1(text, text1):
    return text + ' ' + text1

def fun2(text):
    return text.title()

output = fun2(fun1('MATEUS', 'PEreira'))

print(output)