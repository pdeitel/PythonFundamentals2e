## 9.4 Updating Text Files

### Updating accounts.txt

with (open('accounts.txt', mode='r', encoding='utf-8') as accounts,
      open('temp.txt', mode='x', encoding='utf-8') as temp):
    for record in accounts:
        account, name, balance = record.split()
        temp.write(f'{account} Williams {balance}\n'
            if account == '300' else record)

### os Module File-Processing Functions

import os

os.replace('temp_file.txt', 'accounts.txt')

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
