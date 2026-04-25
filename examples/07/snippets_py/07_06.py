## 7.6 Profiling List vs. array Performance with %timeit

### Timing the Creation of a List of 36,000,000 Die Rolls

import random

%timeit rolls_list = \
    [random.randint(1, 6) for i in range(0, 36_000_000)]

### Timing the Creation of an array Containing Results of 36,000,000 Die Rolls

import numpy as np

rng = np.random.default_rng()

%timeit rolls_array = rng.integers(1, 7, size=36_000_000)

### 360,000,000 and 3,600,000,000 Die Rolls

%timeit rolls_array = rng.integers(1, 7, size=360_000_000)

%timeit rolls_array = rng.integers(1, 7, size=3_600_000_000)

### Customizing the %timeit Iterations

%timeit -n3 -r2 rolls_array = rng.integers(1, 7, size=36_000_000)

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
