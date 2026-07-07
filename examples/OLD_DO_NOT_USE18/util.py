# util.py
"""Utility functions used by various examples."""

import base64
import mimetypes

def base64_encode_file(path):
    """Returns the Base64-encoded data from the file at path."""
    with open(path, 'rb') as file:
        base64_data = base64.b64encode(file.read()).decode()

    return base64_data
        
def create_data_url(path):
    """Guesses MIME type for file at path, then creates a 'data:'
    URL with that MIME type and file's Base64 encoded data."""

    # get image's mime type
    mime_type, _ = mimetypes.guess_type(path)

    # return Base64-encoded files's 'data:' URL 
    return f'data:{mime_type};base64,{base64_encode_file(path)}'

def upload_file(client, path, purpose):
    """Uploads file from path to OpenAI APIs for specified purpose."""
    
    with open(path, 'rb') as file:
        result = client.files.create(file=file, purpose=purpose)

    return result.id













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
