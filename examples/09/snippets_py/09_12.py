## 9.12 Objects-Natural Intro to Data Science: Working with CSV Files

### 9.12.1 Python Standard Library Module csv

### Writing to a CSV File

import csv

with (open('accounts.csv', mode='x', encoding='utf-8',
           newline='') as accounts):
    writer = csv.writer(accounts)
    writer.writerow(['account', 'name', 'balance'])
    writer.writerow([100, 'Perez', 24.98])
    writer.writerow([200, 'Kim', 345.67])
    writer.writerow([300, 'White', 0.00])
    writer.writerow([400, 'Ramos', -42.16])
    writer.writerow([500, 'Borg', 224.62])

### Reading from a CSV File

with (open('accounts.csv', mode='r', encoding='utf-8',
           newline='') as accounts):
    reader = csv.reader(accounts)
    header1, header2, header3 = next(reader)  # get column heads
    print(f'{header1:<10}{header2:<10}{header3:>10}')
    for record in reader:
        account, name, balance = record
        print(f'{account:<10}{name:<10}{balance:>10}')

### Data Containing Commas

### Caution: Commas in CSV Data Fields

### Caution: Missing Commas and Extra Commas in CSV Files

### 9.12.2 Reading CSV Files into Pandas DataFrames

### Datasets

### Working with Locally Stored CSV Files

import pandas as pd

df = pd.read_csv('accounts.csv')

df

df.to_csv('accounts_from_dataframe.csv', index=False)

### 9.12.3 Reading the Titanic Disaster Dataset

### Loading the Titanic CSV Dataset via a URL

import pandas as pd

titanic = pd.read_csv('https://vincentarelbundock.github.io/' +
    'Rdatasets/csv/carData/TitanicSurvival.csv')

### Viewing Some of the Rows in the Titanic Dataset

pd.set_option('display.precision', 2)

titanic.head()

titanic.tail()

### Customizing the Column Names

titanic = titanic.rename(
    columns={'rownames': 'name', 'passengerClass': 'class'})

titanic

### 9.12.4 Simple Data Analysis with the Titanic Disaster Dataset

titanic.describe()

(titanic.survived == 'yes').describe()

### 9.12.5 Passenger Age Histogram

%matplotlib

histogram = titanic.hist(bins=8)

import matplotlib.pyplot as plt

plt.show()

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
