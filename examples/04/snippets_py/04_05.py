## 4.5 Case Study: A Game of Chance

### Sample Outputs

### import Statements

### Function roll_dice—Returning Multiple Values Via a Tuple

### Function display_dice

### enum Type Status

### First Roll

### Subsequent Rolls

### Displaying the Final Results

### Additional Notes on Enum Type GameStatus

from enum import Enum

GameStatus = Enum('GameStatus', ['WON', 'LOST', 'CONTINUE'])

GameStatus.WON.name

GameStatus.WON.value

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
