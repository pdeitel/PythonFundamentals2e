# Fig. 18.2: translate.py
"""Function used to translate text to specified language."""

def translate(client, text, language):
    """Translate text into the specified language using the 
    OpenAI Responses API and return the translation."""

    instructions = f"""You are an expert in natural language translation.
        Translate the input text into {language}."""
    
    response = client.responses.create(model='gpt-5-mini',
        instructions=instructions, input=text)
    
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
