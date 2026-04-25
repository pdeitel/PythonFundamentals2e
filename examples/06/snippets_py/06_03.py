## 6.3 Sets

### Creating a Set with Curly Braces

colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}

colors

### Determining a Set's Length

len(colors)

### Checking Whether a Value Is in a Set

'red' in colors

'purple' in colors

'purple' not in colors

### Iterating Through a Set

for color in colors:
    print(color.upper(), end=' ')

### Creating a Set with the Built-In set Function

numbers = list(range(10)) + list(range(5))

numbers

set(numbers)

set()

### Frozenset: An Immutable Set Type

### 6.3.1 Comparing Sets

{1, 3, 5} == {3, 5, 1}

{1, 3, 5} != {3, 5, 1}

{1, 3, 5} < {3, 5, 1}

{1, 3, 5} < {7, 3, 5, 1}

{1, 3, 5} <= {3, 5, 1}

{1, 3} <= {3, 5, 1}

{1, 3, 5}.issubset({3, 5, 1})

{1, 2}.issubset({3, 5, 1})

{1, 3, 5} > {3, 5, 1}

{1, 3, 5, 7} > {3, 5, 1}

{1, 3, 5} >= {3, 5, 1}

{1, 3, 5} >= {3, 1}

{1, 3} >= {3, 1, 7}

{1, 3, 5}.issuperset({3, 5, 1})

{1, 3, 5}.issuperset({3, 2})

### 6.3.2 Mathematical Set Operations

{1, 3, 5} | {2, 3, 4}

{1, 3, 5}.union([20, 20, 3, 40, 40])

{1, 3, 5} & {2, 3, 4}

{1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4])

{1, 3, 5} - {2, 3, 4}

{1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4])

{1, 3, 5} ^ {2, 3, 4}

{1, 3, 5, 7}.symmetric_difference([2, 2, 3, 3, 4, 4])

{1, 3, 5}.isdisjoint({2, 4, 6})

{1, 3, 5}.isdisjoint({4, 6, 1})

### 6.3.3 Mutable Set Operators and Methods

numbers = {1, 3, 5}

numbers |= {2, 3, 4}

numbers

numbers.update(range(10, 15))

numbers

numbers.add(17)

numbers.add(3)

numbers

numbers.remove(3)

numbers

numbers.pop()

numbers

numbers.clear()

numbers

### 6.3.4 Set Comprehensions

numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]

evens = {item for item in numbers if item % 2 == 0}

evens

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
