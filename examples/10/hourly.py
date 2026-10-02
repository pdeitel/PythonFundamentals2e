# hourly.py
"""Hourly compensation model."""
from decimal import Decimal
from compensationmodel import CompensationModel
from typing import override

class Hourly(CompensationModel):
    """Compensation model for an hourly employee with overtime."""

    def __init__(self, wage: Decimal, hours: Decimal) -> None:
        """Initialize an Hourly compensation model."""

        # if wage is less than 0.00, raise an exception
        if wage < Decimal('0.00'):
            raise ValueError('Wage must be >= 0.00.')

        # if hours is not in the range 0.0-168.0, raise an exception
        if not (Decimal('0.0') <= hours <= Decimal('168.0')):
            raise ValueError('Hours must be >= 0.0 and <= 168.0.')

        self._wage = wage
        self._hours = hours

    @property
    def wage(self) -> Decimal:
        """Return the hourly wage."""
        return self._wage

    @property
    def hours(self) -> Decimal:
        """Return the hours worked."""
        return self._hours

    @override
    def earnings(self) -> Decimal:
        """Calculate earnings, including time-and-a-half overtime."""
        if self.hours <= Decimal('40.0'):
            return self.wage * self.hours

        overtime_hours = self.hours - Decimal('40.0')
        return (Decimal('40.0') * self.wage +
                overtime_hours * self.wage * Decimal('1.5'))

    @override
    def __repr__(self) -> str:
        """Return string representation for repr()."""
        return f'Hourly(wage={self.wage!r}, hours={self.hours!r})'

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
