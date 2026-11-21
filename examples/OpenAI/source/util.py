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


from graphviz import Source
from agents.extensions.visualization import draw_graph

def get_styled_agent_graph(root_agent):
    """Gets an agent visualization in horizontal 
    rather than vertical orientation"""

    # fetch raw read-only source object from the SDK
    original_graph = draw_graph(root_agent)
    
    # extract string code and prepare layout injections
    original_dot_code = original_graph.source
    custom_layout_settings = "\n    rankdir=LR;\n    splines=ortho;\n"
    
    clean_lines = []
    for line in original_dot_code.splitlines():
        clean_lines.append(line)
        
        # inject custom styling right after root digraph declaration
        if "digraph G {" in line:
            clean_lines.append(custom_layout_settings)
            
    # join lines back together into a valid DOT string
    modified_dot_code = "\n".join(clean_lines)
    
    # return new Graphviz object using processed string
    return Source(modified_dot_code)










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
