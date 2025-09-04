# Number guessing game

import random

computer=random.choice(range(1,5))

while True:
    Player=int(input('Guess a number from 1 to 5 (q to quit) :'))
    if Player >5 or Player<1:
        print(f'{Player} is out of range enter a number a 1 to 5')
    elif Player !=computer:
        print('Try again ')
    else:
        print('You won')
        break


