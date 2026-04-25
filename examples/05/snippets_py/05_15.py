## 5.15 Other Sequence Processing Functions

### Customizing How Elements Are Compared By min and max

'Red' < 'orange'

ord('R')

ord('o')

colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']

min(colors, key=lambda s: s.lower())

max(colors, key=lambda s: s.lower())

### Case-Insensitive Sorting

colors

sorted(colors, key=lambda s: s.lower())

colors

### Iterating Backward Through a Sequence

numbers = [1, 2, 3, 4, 5]

reversed_numbers = [item ** 2 for item in reversed(numbers)]

reversed_numbers

### Combining Iterables into Tuples of Corresponding Elements

names = ['Jose', 'Sue', 'Hana']

grade_point_averages = [3.5, 4.0, 3.75]

for name, gpa in zip(names, grade_point_averages):
    print(f'Name={name}; GPA={gpa}')

names.append('Paul')

for name, gpa in zip(names, grade_point_averages, strict=True):
    print(f'Name={name}; GPA={gpa}')

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
