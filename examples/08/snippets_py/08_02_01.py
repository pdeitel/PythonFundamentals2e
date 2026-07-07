## 8.2.1 Presentation Types

f'{17.489:.2f}'

### Integers

f'{10:d}'

num = 1_000_000

f'{num:d}  {num:b} {num:o}  {num:x}  {num:X}'

### Characters

f'{0x1F600:c}  {65:c}  {97:c}'

### Strings

f'{"hello":s} {7}'

f'{"hello":s} {7}'

### Floating-Point and Decimal Values

from decimal import Decimal

f'{Decimal("10_000_000_000_000_000_000_000_000.0"):.3f}'

f'{Decimal("10_000_000_000_000_000_000_000_000.0"):.3e}'

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
