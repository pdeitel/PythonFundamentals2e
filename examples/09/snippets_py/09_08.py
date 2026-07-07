## 9.8 Handling Exceptions

### 9.8.1 Division by Zero and Invalid Input

### Division By Zero

10 / 0

### Invalid Input

value = int(input('Enter an integer: '))

### 9.8.2 try Statements

### try Clause

### except Clause

### else Clause

### Flow of Control for a ZeroDivisionError

### Flow of Control for a ValueError

### Flow of Control for a Successful Division

### Easier to Ask Forgiveness than Permission (EAFP)

### 9.8.3 Catching Multiple Exceptions in One except Clause

### 9.8.4 What Exceptions Does a Function or Method Raise?

### 9.8.5 What Code Should Be Placed in a try Suite?

### 9.8.6 Adding Notes to Exception Objects

try:
    print(10 / 0)
except ZeroDivisionError as e:
    e.add_note('Denominator must be non-zero.')
    raise  # re-raise the current exception

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
