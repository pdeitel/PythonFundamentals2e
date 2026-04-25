## 5.13 Generator Expressions and Generator Functions

### Checkpoint 1 Snippets

### Checkpoint 2 Snippets

numbers = [10, 3, 7, 1, 9, 4, 2]

list(x ** 3 for x in numbers if x % 2 == 0)

### Checkpoint 3 Snippets

def value_and_cube(values):
    """Returns each value and its cube on demand as a tuple"""
    for value in values:
        yield (value, value ** 3)

numbers = [1, 2, 3, 4, 5]

list(value_and_cube(numbers))

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
