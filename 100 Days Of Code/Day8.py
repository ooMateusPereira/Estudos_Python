# Quantas semanas até os 90 anos.

def life_in_weeks(age):
    left = (90 - age)
    week = (left * 52)
    return week

age = 20
weeks = life_in_weeks(age)

print(f'You have {weeks} weeks left.')

# Forma da professora 

def life_in_weeks(age):
    left = 90 - age
    weeks = left * 52
    print(f'You have {weeks} weeks left.')

life_in_weeks(12)

# Eu posso por quantos argumentos eu quiser dentro da função

def func(name, loc):
    print(name)
    print(loc)

func('Mateus', 'RJ')

# Calcular quantas vezes uma letra aparece em um nome.

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")