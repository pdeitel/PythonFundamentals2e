## 10.2 Custom Class Account

### 10.2.1 Test-Driving Class Account

from account import Account

from decimal import Decimal

account1 = Account('Sofia Lopez', Decimal('50.00'))

account1.name

account1.balance

account1.deposit(Decimal('25.53'))

account1.balance

account1.deposit(Decimal('-123.45'))

### 10.2.2 Account Class Definition

Account?

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
