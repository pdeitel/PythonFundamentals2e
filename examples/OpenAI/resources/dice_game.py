from enum import Enum
import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return (die1, die2)  

def display_dice(dice):
    die1, die2 = dice  
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')

GameStatus = Enum('GameStatus', ['WON', 'LOST', 'CONTINUE'])

die_values = roll_dice()  
display_dice(die_values)

sum_of_dice = sum(die_values)

match sum_of_dice:
    case 7 | 11: 
        game_status = GameStatus.WON
    case 2 | 3 | 12:
        game_status = GameStatus.LOST
    case _:  
        game_status = GameStatus.CONTINUE
        my_point = sum_of_dice
        print('Point is', my_point)

while game_status == GameStatus.CONTINUE:
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point:
        game_status = GameStatus.WON
    elif sum_of_dice == 7:  
        game_status = GameStatus.LOST

print('Player wins' if game_status == GameStatus.WON else 'Player loses')

