## 10.6.4 Displaying Card Images with Matplotlib

from deck import DeckOfCards

deck_of_cards = DeckOfCards()

%matplotlib

from pathlib import Path

path = Path('.') / 'card_images'

import matplotlib.pyplot as plt

import matplotlib.image as mpimg

figure, axes = plt.subplots(nrows=4, ncols=13)

for plot in axes.ravel():
    plot.get_xaxis().set_visible(False)
    plot.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread((path / image_name).resolve())
    plot.imshow(img)

figure.tight_layout()

deck_of_cards.shuffle()

for plot in axes.ravel():
    plot.get_xaxis().set_visible(False)
    plot.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread((path / image_name).resolve())
    plot.imshow(img)

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
