## 5.3 Tuples

### Creating an Empty Tuple

student_tuple = ()

student_tuple

len(student_tuple)

### Packing a Tuple Does Not Require Parentheses

student_tuple = 'Lea', 'Dubois', 3.3

student_tuple

len(student_tuple)

another_student_tuple = ('James', 'Roy', 3.7)

another_student_tuple

### Creating a Tuple of One Element

a_singleton_tuple = ('red',)  # note the comma

a_singleton_tuple

not_a_tuple = ('red')  # redundant parentheses

not_a_tuple

type(not_a_tuple)

### Accessing Tuple Elements

time_tuple = (9, 16, 1)

time_tuple

time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2]

### Adding Items to a String or Tuple

tuple1 = (10, 20, 30)

tuple2 = tuple1  # both variables refer to the same tuple object

tuple2

tuple1 += (40, 50)

tuple1

tuple2

### Appending Tuples to Lists

numbers = [1, 2, 3, 4, 5]

numbers += (6, 7)

numbers

### Tuples May Contain Mutable Objects

student_tuple = ('Xinyi', 'Chen', [98, 75, 87])

student_tuple[2][1] = 85

student_tuple

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
