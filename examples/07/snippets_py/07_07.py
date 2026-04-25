## 7.7 array Operators

### Arithmetic Operations with arrays and Individual Numeric Values

import numpy as np

numbers = np.arange(1, 6)

numbers

numbers * 2

numbers ** 3

numbers  # numbers is unchanged by the arithmetic operators

numbers += 10

numbers

### Broadcasting

### Arithmetic Operations Between arrays

numbers2 = np.linspace(1.1, 5.5, 5)

numbers2

numbers * numbers2

### Comparing arrays

numbers3 = np.array([1, 2, 3, 4, 5])

numbers3 >= 3

numbers4 = np.array([2, 2, 2, 2, 2])

numbers3 < numbers4

numbers3 == numbers4

numbers3 == numbers3

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
