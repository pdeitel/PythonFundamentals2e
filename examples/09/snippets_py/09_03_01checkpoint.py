## 9.3.1 Writing to a Text File: Introducing the with Statement

### Checkpoint 1 Snippets

### Checkpoint 2 Snippets

### Checkpoint 3 Snippets

with open('grades.txt', mode='x', encoding='utf-8') as grades:
    grades.write('1 Diaz A\n')
    grades.write('2 Laine B\n')
    grades.write('3 Ali A\n')

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
