## 2.9 Objects-Natural Case Study: Creating and Using Objects of Built-In Type str

### Test-Driving Class str

### Creating str Objects

s1 = 'happy'

s1

s2 = ' birthday'

s2

s3 = ''  # uses two single quotes to create an empty string

s3

### Software Reuse

### Determining a String's Length

len(s1)

len(s2)

len(s3)

### Comparing Strings

s1 == 'happy'

s1 == s2

s1 == 'Happy'

### Testing for Empty Strings and Performing String Concatenation

if len(s3) == 0:
    print('s3 is empty; assigning result of s1 + s2 to s3')
    s3 = s1 + s2  # string concatenation

s3

len(s3)

### str Methods startswith and endswith

s1.startswith('ha')

s2.startswith('ha')

s1.endswith('ay')

s2.endswith('ay')

### Case-Sensitive Comparisons

s1.startswith('HA')

s2.endswith('AY')

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
