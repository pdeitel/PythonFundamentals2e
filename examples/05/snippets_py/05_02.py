## 5.2 Lists

### Creating a List

c = [-45, 6, 0, 72, 1543]

c

### Accessing Elements of a List

c[0]

c[4]

### Determining a List's Length

len(c)

### Accessing Elements from the End of the List with Negative Indices

c[-1]

### Indices Must Be Integers or Integer Expressions

a = 1

b = 2

c[a + b]

### Lists Are Mutable

c[4] = 17

c

### Some Sequences Are Immutable

s = 'hello'

s[0]

s[0] = 'H'

### Attempting to Access a Nonexistent Element

c[100]

### Using List Elements in Expressions

c[0] + c[1] + c[2]

### Appending to a List with +=

colors = ['red', 'orange', 'yellow', 'green', 'blue']

colors += ['indigo', 'violet']

colors

letters = []

letters += 'Python'

letters

### Concatenating Sequences with +

list1 = [10, 20, 30]

list2 = [40, 50]

concatenated_list = list1 + list2

concatenated_list

(1, 2, 3) + (4, 5)

'happy ' + 'birthday'

### Using for and range to Access List Indices and Values

for i in range(len(concatenated_list)):
    print(f'{i}: {concatenated_list[i]}')

### Comparison Operators

a = [1, 2, 3]

b = [1, 2, 3]

c = [1, 2, 3, 4]

a == b  # True: corresponding elements in both are equal

a == c  # False: a and c have different elements and lengths

a < c  # True: a has fewer elements than c

c >= b  # True: elements 0-2 are equal, but c has more elements

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
