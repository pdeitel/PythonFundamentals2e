## 10.9 Duck Typing and Polymorphism

from decimal import Decimal

class WellPaidDuck:
    def __repr__(self):
        return 'WellPaidDuck()'
        
    def earnings(self):
        return Decimal('1_000_000.00')

from employee import Employee

from salaried import Salaried

from commission import Commission

employee1 = Employee('Pierre Simon',
    Salaried(Decimal('800.00')))

employee2 = Employee('Sierra Dembo',
    Commission(Decimal('10000.00'), Decimal('0.06')))

duck = Employee('Duck', WellPaidDuck())

employees = [employee1, employee2, duck]

for employee in employees:
    print(employee)
    print(f'{employee.earnings():,.2f}\n')

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
