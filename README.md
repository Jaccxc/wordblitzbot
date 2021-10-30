# Wordblitz
Word Blitz is a game from Facebook Messenger. Everyone could play it on your phone or computer as long as you have a Facebook account. The game is simple. Given a 4x4 list of characters, connect characters that can make a word. Find as many word combinations as possible in 2 minutes.

## Algorithm
By creating a dictionary with all English words, we can then use this dictionary to find all the possible solutions. 

This script first takes a screenshot from the starting of the game. Then we crop and do some color corrections on it. I found it difficult to correctly recognize the characters by simply sending the processed image to the OCR part, so the script would further merge the processed images.

After the characters are read out from the screenshot, I apply a recursive search starting from top left. Once found a possible solution that matches one word in the dictionary, the script then controls the cursor.

## Usage
You need pytesseract to run this. 
```linux
apt-get install pytesseract
```
After install, first run setwindow.py to set up the correct window for the script.
```linux
python3 setwindow.py
```
Get to the step where the game is about to start, then run pathfinder.py.
```linux
python3 pathfinder.py
```

## Example
![ok](https://github.com/Jaccxc/jacc_css/blob/master/docs/video/ezgif-4-589e8834b8c6.gif)
