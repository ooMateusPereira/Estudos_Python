# Find de the bug.
def fun():
    for i in range(1, 20): # The bug is because de range is just into 19. To fix it, just chenge 20 for 21.
        if i == 20:
            print('Good job.')
fun()

# Find the bug.
from random import randint
dice_images = ['1', '2', '3', '4', '5', '6']
dice_num = randint(1, 6) # The list need be between 0 and 5.
print(dice_images(dice_num)) # Its to use [] not () in dice_num.

# Find the bug.
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994: # Where we have a True and a False togheter. Em True + False = False.
    print('You are a Millenial.')
elif year > 1994:
    print('You are a Gen Z.')
# 1994 needs be include in Millenial or Gen Z using >= or <=. 

# Exception. Its good to prevent the crash a system.
try:
    age = int(input('How old are you?'))
except ValueError:
    print('Invalid format. Try to use numbers.')
    age = int(input('How old are you?'))
if age > 18:
    print('You can drive now.')

# Target is the number up to which we count
def fizz_buzz(target):
    number = []
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])

def fizz_buzz(target):
    for number in range(1, target + 1):
        # use and (not or)
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # use elif (not if)
        elif number % 3 == 0:
            print("Fizz")
        # use elif (not if)
        elif number % 5 == 0:
            print("Buzz")
        else:
            # remove square brackets []
            print(number)