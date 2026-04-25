"""Using Python date/time features to calculate how long a person has been
   alive and determine the day of the week the person was born."""
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
from zoneinfo import ZoneInfo

# prompt for and input locale to use
print('Locale: Input a locale code or press Enter for system default.')
print("Examples: 'es_ES' (Spanish), 'ja_JP' (Japanese)")
locale_input = input('Enter locale code: ').strip()

# set locale for numeric and date/time output
locale.setlocale(locale.LC_NUMERIC, locale_input)
locale.setlocale(locale.LC_TIME, locale_input)

# prompt for and input time zone
print('\nTime zone: Input a time zone or press Enter for system default.')
print("Examples: 'America/New_York', 'Europe/London', 'Asia/Tokyo'")
tz_input = input('Enter time zone: ').strip()

# create ZoneInfo for time zone (or use None for system local time zone)
tz = ZoneInfo(tz_input) if tz_input else None

# read user's birthday and birth time, combine into datetime
birthday_str = input('\nEnter your birthday (YYYY-MM-DD): ').strip()
birth_time_str = input('Enter your birth time (HH:MM): ').strip()
birth_datetime = datetime.fromisoformat(f'{birthday_str} {birth_time_str}')

# attach time zone info if provided
if tz:
    birth_datetime = birth_datetime.replace(tzinfo=tz)
    current_datetime = datetime.now(tz)
else:
    current_datetime = datetime.now()

# display time zone and birth/current datetime for current locale
print(f'\nTime zone: {tz_input if tz_input else "System default"}')
print(f'Birth date/time: {birth_datetime:%c}')
print(f'Current date/time: {current_datetime:%c}')

# calculate years, months, and days alive using relativedelta
delta = relativedelta(current_datetime, birth_datetime)

# calculate the full elapsed time as a timedelta and convert to seconds
elapsed_time = current_datetime - birth_datetime
total_seconds = int(elapsed_time.total_seconds())

# display weekday name of birth date and all calculation results
print(f"""
You were born on a {birth_datetime:%A} and have been alive for:
   {delta.years:n} years
   {delta.months:n} months
   {delta.days:n} days

In individual time units, you have been alive for:
   {delta.years * 12 + delta.months:n} total months
   {elapsed_time.days:n} total days
   {total_seconds // 3600:n} total hours
   {total_seconds // 60:n} total minutes
   {total_seconds:n} total seconds
""")

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
