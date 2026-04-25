## 4.11 Arbitrary Argument Lists

### Defining a Function with an Arbitrary Argument List

def average(*args):
    return sum(args) / len(args)

average(5, 10)

average(5, 10, 15)

average(5, 10, 15, 20)

average()

### Passing an Iterable's Individual Elements as Function Arguments

grades = [88, 75, 96, 55, 83]

average(*grades)

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
