## 3.16 Boolean Operators: and, or, not

### Boolean and Operator

veteran_pilots = 0

employee_type = 'Pilot'

age = 65

if employee_type == 'Pilot' and age >= 63:
    veteran_pilots += 1

veteran_pilots

### Boolean and Operator Truth Table

### Boolean or Operator

semester_average = 83

final_exam = 95

if semester_average >= 90 or final_exam >= 90:
    print('Student gets an A')

### Boolean or Operator Truth Table

### Short-Circuit Evaluation for Improved Performance

### Boolean Operator not

grade = 87

if not (grade == -1):  # parentheses added for clarity
    print(f'The next grade is {grade}')

if grade != -1:
    print(f'The next grade is {grade}')

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
