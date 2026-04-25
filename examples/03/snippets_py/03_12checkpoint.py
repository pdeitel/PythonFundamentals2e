## 3.12 Program Development: Sentinel-Controlled Iteration

### Checkpoint 1 Snippets

### Checkpoint 2 Snippets

### Checkpoint 3 Snippets

# AverageTemperature.py — Fahrenheit average calculator with sentinel value 999
print('Enter Fahrenheit temperatures one at a time.')

total = 0
count = 0

temp = int(input('Enter -212 to 212 (999 to quit): '))

while temp != 999:
    total += temp
    count += 1
    temp = int(input('Enter -212 to 212 (999 to quit): '))

if count > 0:
    average = total / count
    print(f'\nAverage temperature: {average:.2f}')
else:
    print('\nNo temperatures entered.')

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
