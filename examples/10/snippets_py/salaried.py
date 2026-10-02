# salaried.py
"""Salaried compensation model."""
from decimal import Decimal
from compensationmodel import CompensationModel
from typing import override

class Salaried(CompensationModel):
    """Compensation model for an employee paid a fixed weekly salary."""

    def __init__(self, salary: Decimal) -> None:
        """Initialize a Salaried compensation model."""

        # if salary is less than 0.00, raise ValueError
        if salary < Decimal('0.00'):
            raise ValueError('Salary must be >= 0.00.')

        self._salary = salary

    @property
    def salary(self) -> Decimal:
        """Return the salary."""
        return self._salary

    @override
    def earnings(self) -> Decimal:
        """Calculate earnings."""
        return self.salary

    @override
    def __repr__(self) -> str:
        """Return string representation for repr()."""
        return f'Salaried(salary={self.salary!r})'

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
