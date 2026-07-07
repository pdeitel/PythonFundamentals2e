# Fig. 18.7: moderation.py
"""Functions that send text to the OpenAI Moderation API to check
for offensive content and display the moderation results."""

def check_prompt(client, text):
    """ Sends text to OpenAI's Moderation API and returns a
    Moderation object containing the results."""
    
    response = client.moderations.create(
        model='omni-moderation-latest', input=text)
    
    # response.results is a list of Moderation objects.
    # The list contains one element in this example.
    return response.results[0]

def display_moderation_results(result):
    """Receives a Moderation result object and displays its contents."""

    if not result.flagged:
        print('Prompt not flagged for offensive content')
    else:
        print('Offensive content categories & scores:')
        categories = result.categories.model_dump(by_alias=True)
        category_scores = result.category_scores.model_dump(by_alias=True)

        for category, flag in categories.items():
            score = category_scores[category] # get score
            print(f'{category:>25}: {"True" if flag else "False":>5} ' +
                  f'{score if score else 0:.2f}')

def check_image(client, url):
    """ Sends an image's URL to OpenAI's Moderation API and 
    returns a Moderation object containing the results."""
    
    response = client.moderations.create(
        model='omni-moderation-latest', 
        input=[{'type': 'image_url', 
                'image_url': {'url': url}}])
    
    # response.results is a list of Moderation objects.
    # The list contains one element in this example.
    return response.results[0]
    













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
