## 3.18 Intro to Data Science: Measures of Central Tendency—Mean, Median and Mode

### Calculating the Average (Mean) with Built-In Functions sum and len

grades = [85, 93, 45, 89, 85]

sum(grades) / len(grades)

### statistics Module Functions mean, median and mode

import statistics

statistics.mean(grades)

statistics.median(grades)

statistics.mode(grades)

### Sorting a list to Confirm Its Median and Mode

sorted(grades)

### statistics Functions mode and Function multimode

grades2 = [85, 93, 45, 89, 85, 93]

statistics.mode(grades2)

statistics.multimode(grades2)

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
