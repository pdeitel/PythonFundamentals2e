# fig04_02.py
"""Simulating the dice game craps."""
from enum import Enum
import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return (die1, die2)  # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')

# Enum type with constants WON, LOST and CONTINUE representing game status
GameStatus = Enum('GameStatus', ['WON', 'LOST', 'CONTINUE'])

die_values = roll_dice()  # first roll
display_dice(die_values)

# determine game status and point, based on first roll
sum_of_dice = sum(die_values)

match sum_of_dice:
    case 7 | 11:  # win
        game_status = GameStatus.WON
    case 2 | 3 | 12:  # lose
        game_status = GameStatus.LOST
    case _:  # default case: remember point
        game_status = GameStatus.CONTINUE
        my_point = sum_of_dice
        print('Point is', my_point)

# continue rolling until player wins or loses
while game_status == GameStatus.CONTINUE:
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point:  # win by making point
        game_status = GameStatus.WON
    elif sum_of_dice == 7:  # lose by rolling 7
        game_status = GameStatus.LOST

# display "wins" or "loses" message
print('Player wins' if game_status == GameStatus.WON else 'Player loses')

##########################################################################
# (C) Copyright 1992-2026 by Deitel & Associates, Inc. and               #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
