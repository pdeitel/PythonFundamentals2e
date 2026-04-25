## 5.16 Two-Dimensional Lists

### Creating a Two-Dimensional List

values = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]

### List of Lists

len(values)

len(values[0])  # row 0

### Accessing the Elements with Nested Loops

for row in values:
    for item in row:
        print(item, end=' ')
    print()

for i, row in enumerate(values):
    for j, item in enumerate(row):
        print(f'values[{i}][{j}]={item} ', end=' ')
    print()

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
