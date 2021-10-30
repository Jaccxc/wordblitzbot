# Wordblitz bot
This is a python script for WordBlitz, a game on Facebook.
## Algorithim
By creating a dictionary with all English words, we can then use this dictionary to find all the possible solutions. 

This script first takes a screenshot from the starting of the game. Then we crop and do some color corrections on it. I found it difficult to correctly recognize the characters by simply sending the processed image to the OCR part, so the script would further merge the processed images.

After the characters are read out from the screenshot, I apply a recursive search starting from top left. Once found a possible solution that matches one word in the dictionary, the script then controls the cursor.

## Screenshot

