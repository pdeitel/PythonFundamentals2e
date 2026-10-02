## 10.8.2 CompensationModel Subclasses: Salaried and Commission

from decimal import Decimal

from salaried import Salaried

salaried = Salaried(Decimal('800.00'))

salaried

print(f'{salaried.earnings():,.2f}')

Salaried(Decimal('-1.00'))

from commission import Commission

from decimal import Decimal

commission = Commission(Decimal('10000.00'), Decimal('0.06'))

commission

print(f'{commission.earnings():,.2f}')

from compensationmodel import CompensationModel

issubclass(Salaried, CompensationModel)

isinstance(commission, CompensationModel)

isinstance(commission, Salaried)

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
