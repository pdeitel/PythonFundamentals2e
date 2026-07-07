# Fig. 18.1: describe_image.py
"""Function to get accessible image descriptions."""

import util

def describe_image(client, prompt, path_to_image):
    """Generates detailed, accessible image descriptions using the 
       OpenAI Responses API. Works with common image types."""
    
    # construct Base64-encoded image's URL for Responses API
    url = util.create_data_url(path_to_image)
    
    instructions = """
        You are an expert at creating detailed, accessible image
        descriptions per the World Wide Web Consortium's Web Content 
        Accessibility Guidelines (WCAG). Given an image, explain it 
        in detail for people who are blind or have low vision. 
        Identify objects accurately."""

    # Multimodal inputs require a list of dicts, each with the key-value 
    # pair 'role': 'user' (indicating this is the user's data on which to
    # operate) and a 'content' key. When uploading an image, this key's 
    # value is a list of dicts. One dict must have the key-value pair
    # 'type': 'input_image' and the key 'image_url' for which the value is
    # the data URL containing the Base64-encoded image. Optionally, you 
    # can provide a prompt via a dict containing the key-value pair 
    # 'type': 'input_text' and the key 'text' with the prompt as a value.
    response = client.responses.create(
        model='gpt-5-mini',
        instructions=instructions,
        input=[
            {
                'role': 'user',
                'content': [
                    {'type': 'input_text', 'text': prompt},
                    {'type': 'input_image', 'image_url': url}
                ]
            }
        ]
    )

    return response.output_text














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

