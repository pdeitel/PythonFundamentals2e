## 6.3 Sets

### 6.3 Checkpoint Snippets

text = 'to be or not to be that is the question'

unique_words = set(text.split())

for word in sorted(unique_words):
    print(word, end=' ')

### 6.3.1 Checkpoint Snippets

set('abc def ghi jkl mno').issuperset('hi mom')

### 6.3.2 Checkpoint Snippets

{10, 20, 30} - {5, 10, 15, 20}

{10, 20, 30} ^ {5, 10, 15, 20}

{10, 20, 30} | {5, 10, 15, 20}

{10, 20, 30} & {5, 10, 15, 20}

### 6.3.3 Checkpoint Snippets

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
