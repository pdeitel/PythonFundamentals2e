## 10.8.4 Processing Employee Payroll Polymorphically

### Checkpoint 1 Snippets

### Checkpoint 2 Snippets

from hourly import Hourly

hourly = Hourly(Decimal('25.00'), Decimal('45.0'))

employee3 = Employee('Lin Wong', hourly)

employees.append(employee3)

for employee in employees:
    print(employee)
    print(f'{employee.earnings():,.2f}\n')

### Checkpoint 1 Snippets

### Checkpoint 2 Snippets

### Checkpoint 3 Snippets

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
