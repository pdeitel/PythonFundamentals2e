## 5.14 Reductions and an Intro to lambda Expressions

### Checkpoint 1 Snippets

### Checkpoint 2 Snippets

from functools import reduce

numbers = [10, 20, 30, 40, 50]

reduce(lambda x, y: x + y * y, numbers, 0)

### Checkpoint 3 Snippets

numbers2 = [5, 2, 1, 4, 3]

reduce(lambda x, y: x if x <= y else y, numbers2)  # minimum

reduce(lambda x, y: x if x >= y else y, numbers2)  # maximum

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
