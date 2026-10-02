# employee.py
"""Employee class. An Employee "has a" CompensationModel."""
from decimal import Decimal
from compensationmodel import CompensationModel
from typing import override

class Employee:
    """An Employee with a name and a CompensationModel."""

    def __init__(self, name: str,
                compensation_model: CompensationModel) -> None:
        """Initialize an Employee's name and CompensationModel."""
        self._name = name
        self.compensation_model = compensation_model

    @property
    def name(self) -> str:
        """Return the Employee's name."""
        return self._name

    @property
    def compensation_model(self) -> CompensationModel:
        """Return the Employee's CompensationModel."""
        return self._compensation_model

    @compensation_model.setter
    def compensation_model(self, model: CompensationModel) -> None:
        """Set the Employee's CompensationModel."""
        self._compensation_model = model

    def earnings(self) -> Decimal:
        """Calculate earnings using the Employee's CompensationModel."""
        return self.compensation_model.earnings()

    @override
    def __repr__(self) -> str:
        """Return string representation for repr()."""
        return (f'Employee(name={self.name!r}, ' +
                f'compensation_model={self.compensation_model!r})')

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
