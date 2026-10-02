## 10.8.2 CompensationModel Subclasses: Salaried and Commission

### Checkpoint 1 Snippets

### Checkpoint 2 Snippets

from decimal import Decimal

from hourly import Hourly

pay_model = Hourly(Decimal('20.00'), Decimal('50.0'))

pay_model

print(f'{pay_model.earnings():,.2f}')

pay_model = Hourly(Decimal('20.00'), Decimal('30.0'))

print(f'{pay_model.earnings():,.2f}')

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
