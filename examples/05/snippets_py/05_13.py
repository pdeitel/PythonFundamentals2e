## 5.13 Generator Expressions and Generator Functions

### Creating a Generator Expression

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

for value in (x ** 2 for x in numbers if x % 2 != 0):
    print(value, end=' ')

### Generator Expressions Do Not Create Lists

squares_of_odds = (x ** 2 for x in numbers if x % 2 != 0)

squares_of_odds

### Generator Expressions Can Be Passed as a Function's Iterable Argument

sum(squares_of_odds)

### Generator Functions

def square_generator(values):
    """Square values' items, yielding one at a time on demand"""
    for value in values:
        yield value ** 2

numbers = list(range(1, 4))

numbers

for square in square_generator(numbers):
    print(square, end=' ')
print()

### Built-In Functions filter and map

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
