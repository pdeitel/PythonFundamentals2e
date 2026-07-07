## 9.5 Objects-Natural Case Study: JSON Serialization and Deserialization

### Checkpoint 1 Snippets

### Checkpoint 2 Snippets

### Checkpoint 3 Snippets

import json

grades_dict = {'gradebook':
    [{'student_id': 1, 'name': 'Red', 'grade': 'A'},
     {'student_id': 2, 'name': 'Green', 'grade': 'B'},
     {'student_id': 3, 'name': 'White', 'grade': 'A'}]}

with open('grades.json', mode='x', encoding='utf-8') as grades:
    json.dump(grades_dict, grades, ensure_ascii=False)

with open('grades.json', mode='r', encoding='utf-8') as grades:
    print(json.dumps(json.load(grades), indent=4))

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
