# image_edits.py
"""Functions for image editing with the OpenAI APIs."""

import base64
from pathlib import Path
import util # for our utility functions in util.py

def restyle_with_images_api(
    client, image_path, output_path, size, style_prompt):
    """Restyles a photo using a style prompt. 
    Uses gpt-image-1 via the Images Edits API. """

    # perform style-transfer edit via a text prompt
    with open(image_path, 'rb') as image_file:
        response = client.images.edit(model='gpt-image-1',
            image=image_file, size=size, prompt=style_prompt)

    # output bytes to path    
    output_path.write_bytes(base64.b64decode(response.data[0].b64_json))
    print(f'Image stored in:\n{output_path}')

def restyle_with_responses_api(client, to_image_path, from_image_path, 
    output_path, size, style_prompt=None):
    """Restyles a photo using the style of another image 
    via the Responses API and the gpt-5-mini model."""

    prompt = f"""Apply the style of the second image to the first. 
        Keep the subject's identity and layout. Output size: {size}.
        Additional details from caller: {(style_prompt or 'None')}""" 

    response = client.responses.create(
        model='gpt-5-mini',
        tools=[{'type': 'image_generation'}],
        input=[{
            'role': 'user',
            'content': [
                {'type': 'input_text', 'text': prompt},
                {'type': 'input_image',
                 'image_url': util.create_data_url(to_image_path)},
                {'type': 'input_image',
                 'image_url': util.create_data_url(from_image_path)},
            ],
        }],
    )

    # get the image_generation tool result (base64-encoded PNG)
    image_calls = [output for output in response.output
                       if output.type == 'image_generation_call']

    if image_calls:
        base64_image = image_calls[0].result # Base64-encoded image
        Path(output_path).write_bytes(base64.b64decode(base64_image))
        print(f'Image stored in:\n{output_path}')
    else:
        print('No image generated')















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
