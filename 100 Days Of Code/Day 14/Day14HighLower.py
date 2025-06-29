from os import name
import random 
from Dictionary import data
from Logo import art1
from Logo import art2

random_person_a = random.randint(0, 21)
random_person_b = random.randint(0, 21)
person_a = data[random_person_a]
person_b = data[random_person_b]
game_on = True
score = 0

def HigherLower():

    print(art1)

    while game_on:

            
            print(f'Compare A:', person_a['name'] +',', person_a['description'] + ', from',  person_a['country'] + '.')
            print(art2)
            print(f'Compare B:', person_b['name'] +',', person_b['description'] + ', from',  person_b['country'] + '.')
            
            answer = input("Who has more followers? Type 'A' or 'B': ").lower()
            
            
            if answer == 'a':
                if person_a['followers_count'] > person_b['followers_count']:
                    print(f"\nRight answer! {person_a['name']} has {person_a['followers_count']} million followers.")
                    print(f"{person_b['name']} has {person_b['followers_count']} million followers.\n")
                    score += 1
                    print(f'Your current score is: {score}\n')
                else:
                    print(f"\nWrong answer! {person_b['name']} has {person_b['followers_count']} million followers.")
                    print(f"{person_a['name']} has {person_a['followers_count']} million followers.\n")
                    score -= 1 # Subtract point if the answer is wrong
                    print(f'Your current score is: {score}\n')
            elif answer == 'b':
                if person_b['followers_count'] > person_a['followers_count']:
                    print(f"\nRight answer! {person_b['name']} has {person_b['followers_count']} million followers.")
                    print(f"{person_a['name']} has {person_a['followers_count']} million followers.\n")
                    score += 1
                    print(f'Your current score is: {score}\n')
                else:
                    print(f"\nWrong answer! {person_a['name']} has {person_a['followers_count']} million followers.")
                    print(f"{person_b['name']} has {person_b['followers_count']} million followers.\n")
                    score -= 1 # Subtract point if the answer is wrong
                    print(f'Your current score is: {score}\n')
            else:
                print('\nInvalid option! Please choose "a" or "b".\n')
                # You could add a score -= 1 here as well, depending on your game logic.
                print(f'Your current score is: {score}\n')      
            
HigherLower()