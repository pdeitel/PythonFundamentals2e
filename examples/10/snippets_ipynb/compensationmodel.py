# compensationmodel.py
"""CompensationModel abstract superclass."""
from abc import ABC, abstractmethod
from decimal import Decimal

class CompensationModel(ABC):
    """Abstract superclass specifying compensation model methods."""

    @abstractmethod
    def earnings(self) -> Decimal:
        """Calculate earnings. Subclasses must override this method."""
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        """Return string representation for repr().
        Subclasses must override this method."""
        raise NotImplementedError

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
