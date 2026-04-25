## 6.2 Dictionaries

### 6.2.1 Creating a Dictionary

country_codes = {'Finland': 'fi', 'South Africa': 'za',
                 'Nepal': 'np'}

country_codes

len(country_codes)

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

country_codes.clear()

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

keys = ['Finland', 'South Africa', 'Nepal']

values = ['fi', 'za', 'np']

dict(zip(keys, values))

### 6.2.2 Iterating through Key–Value Pairs

days_per_month = {'January': 31, 'February': 28, 'March': 31}

days_per_month

for month, days in days_per_month.items():
    print(f'{month} has {days} days')

for month, days in reversed(days_per_month.items()):
    print(f'{month} has {days} days')

for month in days_per_month:
    print(month, end=' ')

### 6.2.3 Basic Dictionary Operations

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

roman_numerals

roman_numerals['V']

roman_numerals['X'] = 10

roman_numerals

roman_numerals['L'] = 50

roman_numerals

del roman_numerals['III']

roman_numerals

roman_numerals.pop('X')

roman_numerals

roman_numerals['III']

roman_numerals.get('III')

roman_numerals.get('III', 'III not in dictionary')

roman_numerals.get('V')

'V' in roman_numerals

'III' in roman_numerals

'III' not in roman_numerals

### 6.2.4 Dictionary Methods keys and values

months = {'January': 1, 'February': 2, 'March': 3}

for month_name in months.keys():
    print(month_name, end=' ')

for month_number in months.values():
    print(month_number, end=' ')

months_view = months.keys()

for key in months_view:
    print(key, end=' ')

months['December'] = 12

months

for key in months_view:
    print(key, end=' ')

list(months.keys())

list(months.values())

list(months.items())

for month_name in sorted(months.keys()):
    print(month_name, end=' ')

### 6.2.5 Dictionary Comparisons

country_capitals1 = {'Belgium': 'Brussels',
                     'Haiti': 'Port-au-Prince'}

country_capitals2 = {'Nepal': 'Kathmandu',
                     'Uruguay': 'Montevideo'}

country_capitals3 = {'Haiti': 'Port-au-Prince',
                     'Belgium': 'Brussels'}

country_capitals1 == country_capitals2

country_capitals1 == country_capitals3

country_capitals1 != country_capitals2

### 6.2.6 Example: Dictionary of Student Grades

### 6.2.7 Example: Dictionary of Word Counts

### 6.2.8 Dictionary Method update and the Dictionary Union Operators

country_codes = {}

country_codes.update({'South Africa': 'za'})

country_codes

country_codes.update(Australia='au')

country_codes

capitals1 = {'Belgium': 'Brussels',
             'Haiti': 'Port-au-Prince'}

capitals2 = {'Nepal': 'Kathmandu',
             'Uruguay': 'Montevideo'}

capitals1 | capitals2

capitals1

capitals2

capitals1 |= capitals2

capitals1

capitals2

### 6.2.9 Arbitrary Keyword Arguments and Keyword-Only Parameters

def send_email(*, sender, recipient, **kwargs):
    print(f'{sender=}\n{recipient=}')

    # display the optional keyword arguments, if any
    if kwargs:
        for key, value in kwargs.items():
            print(f'{key}={value}')
    else:
        print('\nNo additional keyword arguments.')

send_email(sender='test1@deitel.com',
    recipient='test2@deitel.com')

send_email(sender='test1@deitel.com',
    recipient='test2@deitel.com',
    subject='Testing send_email',
    body='Testing our email simulation function.')

parameters = {
    'sender': 'test1@deitel.com',
    'recipient': 'test2@deitel.com',
    'subject': 'Testing send_email',
    'body': 'Testing our email simulation function.',
}

send_email(**parameters)

### 6.2.10 Dictionary Comprehensions

months = {'January': 1, 'February': 2, 'March': 3}

months2 = {number: name for name, number in months.items()}

months2

months2[2]

grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}

grades2 = {k: sum(v) / len(v) for k, v in grades.items()}

grades2

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
