# Fig. 18.7: speech_to_vtt.py
"""Function to convert audio to closed captions in WebVTT format."""

def speech_to_vtt(client, audio_path):
    """Converts an audio track into WebVTT captions."""

    # transcribe audio with per-segment timestamps (verbose_json)
    with open(audio_path, 'rb') as audio_file:
        vtt = client.audio.transcriptions.create(model='whisper-1',
            file=audio_file, response_format='vtt')
        
    return vtt # return the captions string
















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
