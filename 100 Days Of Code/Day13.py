# Find de the bug.
def fun():
    for i in range(1, 20): # The bug is because de range is just into 19. To fix it, just put 21.
        if i == 20:
            print('Good job.')

fun()