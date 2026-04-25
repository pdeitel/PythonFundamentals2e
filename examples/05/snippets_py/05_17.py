## 5.17 Pattern Matching in match…case Statements

def display_dice(*dice):
    match dice:
        case [1, 1]:  # snake eyes
            print('Player rolled snake eyes: 1 + 1 = 2')
        case [6, 6]:  # boxcars
            print('Player rolled boxcars: 6 + 6 = 12')
        case [x, y] if x == y:  # any other doubles
            print(f'Player rolled doubles: {x} + {y} = {x + y}')
        case [x, y]:  # all other valid rolls
            print(f'Player rolled: {x} + {y} = {x + y}')
        case _:  # "default" case matches any pattern
            print('Invalid argument')

### Matching Literal Values in a Pattern

display_dice(1, 1)

display_dice(6, 6)

### Guarded cases and Assigning Values to Variables

display_dice(4, 4)

### Matching the Remaining Dice Combinations

display_dice(3, 5)

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
