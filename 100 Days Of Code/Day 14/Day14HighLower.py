from os import name
import random 
from Dictionary import data
from Logo import art1
from Logo import art2


def HigherLower():
    print(art1)
    score = 0
    game_on = True
    while game_on: 
            
            random_person = random.randint(0, 21)
            person_a = data[random_person]
            person_b = data[random_person + 1]
            
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
                    score -= 1 
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
                    score -= 1 
                    print(f'Your current score is: {score}\n')
            else:
                print('\nInvalid option! Please choose "a" or "b".\n')
                print(f'Your current score is: {score}\n')  
            
            if score >= 6:
                over = input("\n If you want to stop type 'S': \n").lower()
                if over == 's':
                    game_on = False
            if score <= -3:
                over = input("\n If you want to stop type 'S': \n").lower()
                if over == 's':
                    game_on = False
            
HigherLower()