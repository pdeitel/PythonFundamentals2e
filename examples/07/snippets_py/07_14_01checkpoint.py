## 7.14.1 pandas Series

### Checkpoint 1 Snippets

import numpy as np

import pandas as pd

rng = np.random.default_rng()

temps = rng.integers(60, 101, size=6)

temperatures = pd.Series(temps)  # (a)

temperatures  # (a)

temperatures.min()  # (b)

temperatures.max()  # (b)

temperatures.mean()  # (b)

temperatures.describe()  # (c)

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
