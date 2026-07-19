# Fig. 18.5: create_image.py
"""Function used to create original images."""

import base64

def create_image(client, path, prompt):
    """Generates an original image based on the prompt and
    stores it in the file specified by path."""
    response = client.images.generate(model='gpt-image-1', prompt=prompt)

    # decode Base64-encoded image bytes
    image_bytes = base64.b64decode(response.data[0].b64_json)

    # output bytes to path
    path.write_bytes(image_bytes) 
    print(f'Image stored in:\n{path}')















##########################################################################
# (C) Copyright 2025 by Deitel & Associates, Inc. and                    #
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
