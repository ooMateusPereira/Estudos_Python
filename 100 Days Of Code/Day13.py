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