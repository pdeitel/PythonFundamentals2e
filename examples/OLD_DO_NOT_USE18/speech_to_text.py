# Fig. 18.3: speech_to_text.py
"""Function used to transcribe speech to text."""

def speech_to_text(client, audio_path):
    """Transcribes the audio file at audio_path to text."""
    
    with open(audio_path, 'rb') as audio_file:
        transcript = client.audio.transcriptions.create( 
            model='gpt-4o-transcribe', file=audio_file)
        
    return transcript.text 














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
