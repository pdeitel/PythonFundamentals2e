## 9.3.1 Writing to a Text File: Introducing the with Statement

with open('accounts.txt', mode='x', encoding='utf-8') as accounts:
    accounts.write('100 Perez 24.98\n')
    accounts.write('200 Kim 345.67\n')
    accounts.write('300 White 0.00\n')
    accounts.write('400 Ramos -42.16\n')
    accounts.write('500 Borg 224.62\n')

### Managing a Resource Via the with Statement

### Built-In open Function

### Writing to the File

### Contents of accounts.txt File

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
