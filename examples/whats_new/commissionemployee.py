# commmissionemployee.py
"""CommissionEmployee base class."""
from decimal import Decimal
from typing import override

class CommissionEmployee:
    """An employee who gets paid commission based on gross sales."""

    def __init__(self, name, gross_sales, commission_rate):
        """Initialize CommissionEmployee's attributes."""
        self._name = name
        self.gross_sales = gross_sales  # validate via property
        self.commission_rate = commission_rate  # validate via property

    @property
    def name(self):
        return self._name

    @property
    def gross_sales(self):
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, sales):
        """Set gross sales or raise ValueError if invalid."""
        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= to 0')
        
        self._gross_sales = sales
        
    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, rate):
        """Set commission rate or raise ValueError if invalid."""
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError(
               'Interest rate must be greater than 0 and less than 1')
        
        self._commission_rate = rate

    def earnings(self):
        """Calculate earnings."""   
        return self.gross_sales * self.commission_rate

    @override
    def __repr__(self):
        """Return string representation for repr()."""
        return (f'CommissionEmployee: {self.name}\n' + 
            f'gross sales: {self.gross_sales:.2f}\n' +
            f'commission rate: {self.commission_rate:.2f}')



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
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
