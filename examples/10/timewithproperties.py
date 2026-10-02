# timewithproperties.py
"""Class Time with read-write properties."""

class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour: int = 0, minute: int = 0,
        second: int = 0) -> None:
        """Initialize each attribute."""
        self.hour = hour # 0-23
        self.minute = minute # 0-59
        self.second = second # 0-59

    @property
    def hour(self) -> int:
        """Return the hour."""
        return self._hour

    @hour.setter
    def hour(self, hour: int) -> None:
        """Set the hour."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._hour = hour

    @property
    def minute(self) -> int:
        """Return the minute."""
        return self._minute

    @minute.setter
    def minute(self, minute: int) -> None:
        """Set the minute."""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')

        self._minute = minute

    @property
    def second(self) -> int:
        """Return the second."""
        return self._second

    @second.setter
    def second(self, second: int) -> None:
        """Set the second."""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._second = second

    def set_time(self, hour: int = 0, minute: int = 0,
        second: int = 0) -> None:
        """Set values of hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self) -> str:
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, ' +
                f'second={self.second})')

    def __str__(self) -> str:
        """Return the Time as a 12-hour clock-format string."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:02d}:{self.second:02d}' +
                (' AM' if self.hour < 12 else ' PM'))

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
