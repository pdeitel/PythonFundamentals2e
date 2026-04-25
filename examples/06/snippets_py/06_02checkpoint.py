## 6.2 Dictionaries

### 6.2.1 Checkpoint Snippets

states = {'VT': 'Vermont', 'NH': 'New Hampshire',
          'MA': 'Massachusetts'}

states

keys = ['VT', 'NH', 'MA']

values = ['Vermont', 'New Hampshire', 'Massachusetts']

dict(zip(keys, values))

### 6.2.2 Checkpoint Snippets

grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}

for name, grade_list in grades.items():
    average = sum(grade_list) / len(grade_list)
    print(f"{name}'s average grade is {average:.2f}")

### 6.2.3 Checkpoint Snippets

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

roman_numerals['x'] = 10

roman_numerals

### 6.2.4 Checkpoint Snippets

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}

list(roman_numerals.keys())

list(roman_numerals.values())

list(roman_numerals.items())

### 6.2.5 Checkpoint Snippets

### 6.2.7 Checkpoint Snippets

import random

numbers = [random.randint(1, 5) for i in range(50)]

from collections import Counter

counter = Counter(numbers)

for value, count in sorted(counter.items()):
    print(f'{value:<4}{count}')

### 6.2.10 Checkpoint Snippets

{number: number ** 3 for number in range(1, 6)}

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
