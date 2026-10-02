## 10.8.4 Processing Employee Payroll Polymorphically

from decimal import Decimal

from salaried import Salaried

from commission import Commission

from employee import Employee

salaried = Salaried(Decimal('800.00'))

employee1 = Employee('Pierre Simon', salaried)

employee1

print(f'{employee1.earnings():,.2f}')

commission = Commission(Decimal('10000.00'), Decimal('0.06'))

employee2 = Employee('Sierra Dembo', commission)

employee2

print(f'{employee2.earnings():,.2f}')

employees = [employee1, employee2]

for employee in employees:
    print(employee)
    print(f'{employee.earnings():,.2f}\n')

### 10.8.4 Checkpoint Snippets
from hourly import Hourly

hourly = Hourly(Decimal('25.00'), Decimal('45.0'))

employee3 = Employee('Lin Wong', hourly)

employees.append(employee3)

for employee in employees:
    print(employee)
    print(f'{employee.earnings():,.2f}\n')


### 10.8.5 Design Benefits of Interface Inheritance and Dependency Injection

employee1.compensation_model = Commission(
    Decimal('20000.00'), Decimal('0.1'))

employee1

print(f'{employee1.earnings():,.2f}')

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
