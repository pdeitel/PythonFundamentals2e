## 3.17 Objects-Natural Case Study: Precise Monetary Calculations with Type Decimal

### Floating-Point Numbers Are Approximations

amount = 112.31

print(amount)

print(f'{amount:.20f}')

### Class Decimal from the Python Standard Library's decimal Module

### Importing the Decimal Class from the decimal Module

from decimal import Decimal

### Creating Decimals

x = Decimal('10.5')

x

y = Decimal(2)  # OK because integers are represented exactly

y

print(x)

print(y)

### Decimal Arithmetic

x + y

x // y

x += y

x

Decimal('10.25') * Decimal('5.75')

### Decimal Precision

### Compound-Interest Problem Requirements Statement

### Calculating Compound Interest

principal = Decimal('1000.00')

rate = Decimal('0.05')

for year in range(1, 11):
    amount = principal * (1 + rate) ** year
    print(f'{year:>2}{amount:>10.2f}   {amount}')

### Formatting the Year and Amount on Deposit

### A Policy Issue: Half-Up Rounding vs. Banker's Rounding

### Banker's Rounding

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
