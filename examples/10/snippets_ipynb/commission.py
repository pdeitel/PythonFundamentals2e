# commission.py
"""Commission compensation model."""
from decimal import Decimal
from compensationmodel import CompensationModel
from typing import override

class Commission(CompensationModel):
    """Compensation model for an employee paid commission."""

    def __init__(self, gross_sales: Decimal,
                 commission_rate: Decimal) -> None:
        """Initialize a Commission compensation model."""

        # if gross_sales is less than 0.00, raise ValueError
        if gross_sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= 0.00.')

        # if commission_rate is not between 0.0 and 1.0, raise ValueError
        if not (Decimal('0.0') < commission_rate < Decimal('1.0')):
            raise ValueError(
                'Commission rate must be > 0 and < 1.')

        self._gross_sales = gross_sales
        self._commission_rate = commission_rate

    @property
    def gross_sales(self) -> Decimal:
        """Return the gross sales."""
        return self._gross_sales

    @property
    def commission_rate(self) -> Decimal:
        """Return the commission rate."""
        return self._commission_rate

    @override
    def earnings(self) -> Decimal:
        """Calculate earnings."""
        return self.gross_sales * self.commission_rate

    @override
    def __repr__(self) -> str:
        """Return string representation for repr()."""
        return (f'Commission(gross_sales={self.gross_sales!r}, ' +
                f'commission_rate={self.commission_rate!r})')

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
