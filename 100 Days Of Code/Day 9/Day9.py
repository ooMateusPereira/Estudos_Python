student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = []

for student in student_scores:
    score = student_scores[student]

    if score >= 91:
        print(f'{student}: Outstanding.')
        student_grades += student
    elif score >= 81:
        print(f'{student}: Exceeds Expectations.')
        student_grades += student
    elif score >= 80:
        print(f'{student}: Acceptable.')
        student_grades += student
    elif score >= 71:
        print(f'{student}: Exceeds Expectations.')
        student_grades += student
    else:
        print(f'{student}: Fail.')
        student_grades += student
    

# Versão da professora 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
 
# Create an empty dictionary to collect the new values.
student_grades = {}
 
# Loop through each key in the student_scores dictionary
for student in student_scores:
 
    #Get the value (student score) by using the key each time.
    score = student_scores[student]
 
    #Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'


Acessar um item dentro uma lista dentro de um dicionário
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon']
}
print(travel_log['France'][1])


Acessar uma lista dentro de uma lista
lista = ['a', 'b', ['c', 'd']]
print(lista[2][1])


# Acessar uma lista dentro um dicionário dentro de um dicionário
travel_log = {
    'France': { 
    'cities_visited':['Paris', 'Lille', 'Dijon'],
    'total_visited': 12
    },
    'Germany': { 
    'cities_visited':['Berlin', 'Hamburg', 'Stuttgart'],
    'total_visited': 10
    },
}
print(travel_log['Germany']['cities_visited'][2])

Which line of code will change the starting_dictionary to the final_dictionary?

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary['c'] = 7; 
final_dictionary = starting_dictionary

Which line of code will produce an error?

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

print(dict[1])