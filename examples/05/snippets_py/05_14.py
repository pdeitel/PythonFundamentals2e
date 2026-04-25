## 5.14 Reductions and an Intro to lambda Expressions

### Custom Reductions

def multiply(x, y):
    return x * y

from functools import reduce

numbers = [1, 2, 3, 4, 5]

reduce(multiply, numbers)

### How Reduce Uses multiply

### reduce's Optional Third Argument

### Predefined Functions for Common Operations

from operator import mul

reduce(mul, numbers)

### Lambda Expressions

reduce(lambda x, y: x * y, numbers)

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
