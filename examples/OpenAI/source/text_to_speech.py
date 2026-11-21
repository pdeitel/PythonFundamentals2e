# Fig. 18.4: text_to_speech.py
"""Function used to synthesize speech from text."""

def text_to_speech(client, text, path, voice, instructions=''):
    """Synthesizes speech from the provided text and 
    writes it to the file specified by path."""
    response = client.audio.speech.create(model='gpt-4o-mini-tts',
        voice=voice, input=text, instructions=instructions)

    response.write_to_file(str(path))
    













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
