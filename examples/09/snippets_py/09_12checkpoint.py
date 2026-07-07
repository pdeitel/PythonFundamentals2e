## 9.12 Objects-Natural Intro to Data Science: Working with CSV Files

### 9.12.1 Checkpoint 1 Snippets

### 9.12.1 Checkpoint 2 Snippets

import csv

with (open('grades.csv', mode='x', encoding='utf-8', newline='')
           as grades):
    writer = csv.writer(grades)
    writer.writerow(['id', 'name', 'grade'])
    writer.writerow([1, 'Kim', 'A'])
    writer.writerow([2, 'Perez', 'B'])
    writer.writerow([3, 'Borg', 'A'])

with (open('grades.csv', mode='r', encoding='utf-8',
           newline='') as grades):
    reader = csv.reader(grades)
    header1, header2, header3 = next(reader)  # get column heads
    print(f'{header1:<4}{header2:<7}{header3}')
    for record in reader:
        student_id, name, grade = record
        print(f'{student_id:<4}{name:<7}{grade}')

### 9.12.5 Checkpoint 1 Snippets

### 9.12.5 Checkpoint 2 Snippets

pd.read_csv('grades.csv')

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
