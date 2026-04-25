## 4.4 Random-Number Generation

### Rolling a Six-Sided Die

import random

for roll in range(10):
    print(random.randint(1, 6), end=' ')

for roll in range(10):
    print(random.randint(1, 6), end=' ')

### Rolling a Six-Sided Die 6,000,000 Times

### Seeding the Random-Number Generator for Reproducibility

random.seed(32)

for roll in range(10):
    print(random.randint(1, 6), end=' ')

for roll in range(10):
    print(random.randint(1, 6), end=' ')

random.seed(32)

for roll in range(10):
    print(random.randint(1, 6), end=' ')

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
