## 10.10 Operator Overloading

### 10.10.1 Test-Driving Class Complex

from complexnumber import Complex

x = Complex(real=2, imaginary=4)

x

y = Complex(real=5, imaginary=-1)

y

x + y

x

y

x2 = x # aim x2 at the same Complex object as x

id(x)

id(x2)

x += y # auto-converted to x = x + y

x, id(x) # display x's new value and id

x2, id(x2) # display x2's unchanged value and id

y # y remains unchanged

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
