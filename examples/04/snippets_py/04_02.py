## 4.2 Defining Functions

def square(number):
    """Calculate the square of number."""
    return number ** 2

square(7)

square(2.5)

### Defining a Custom Function

### Specifying a Custom Function's Docstring

### Returning a Result to a Function's Caller

print('The square of 7 is', square(7))

### Other Ways to Return Control to a Function's Caller

### What Happens When You Call a Function?

### Accessing a Function's Docstring via IPython's Help Mechanism

square?

square??

print(square.__doc__)

### Paging through Lengthy Docstrings

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
