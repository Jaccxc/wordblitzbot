import copy
import sys
import gi
import time
import textract
import pytesseract
gi.require_version('Gtk', '3.0')
from gi.repository import Gdk
from pymouse import PyMouse
from PIL import Image, ImageEnhance
from multiprocessing.dummy import Pool
from functools import partial
from itertools import repeat
from pprint import pprint


sys.setrecursionlimit(5000)
def next_character(visited, current_row, current_column, dictionary):
	counter = 0
	if (time.time()-tstart)>90:
		return 0
	if(len(visited) > 7):
		return counter
	word = ""
	visited.append((current_row, current_column))
	for letter in visited:
		word+=board[letter[0]][letter[1]]
	if(word.upper() in dictionary and len(word) > 1):
		if word not in word_candidates:
			word_candidates.append(word)
			print(word)
			print(visited)
			for x,y in visited:
				pym.press(200+142*y, 623+142*x, button=1)
				finalx=200+142*y
				finaly=623+142*x
				print(str(finalx)+' '+str(finaly))
				time.sleep(0.03)
			pym.release(finalx, finaly, button=1)
		# word_candidates.append(word)
	prev_row = current_row - 1
	next_row = current_row + 1
	prev_column = current_column - 1
	next_column = current_column + 1
	# print(word)
	# Adds the charcter S the current pos
	if(len(board[current_row]) > next_row and ((next_row, current_column) not in visited)):
		counter += next_character(copy.deepcopy(visited), next_row, current_column, dictionary)
	#Adds the character SE the current pos
	if(len(board[current_row]) > next_row and len(board) > next_column) and ((next_row, next_column) not in visited):
		counter += next_character(copy.deepcopy(visited), next_row, next_column, dictionary)
	# Adds the charcter E of the current pos
	if(len(board) > next_column and ((current_row, next_column) not in visited)):
		counter += next_character(copy.deepcopy(visited), current_row, next_column, dictionary)
	#Adds the character NE the current pos
	if(len(board) > next_column and prev_row >= 0 and ((prev_row, next_column) not in visited)):
		counter += next_character(copy.deepcopy(visited), prev_row, next_column, dictionary)
	# Adds the charcter N the current pos
	if(prev_row >= 0 and ((current_row -1, current_column) not in visited)):
		counter += next_character(copy.deepcopy(visited), prev_row, current_column, dictionary)
	# Adds the charcter NW of the current pos
	if(prev_row >= 0 and prev_column >= 0 and ((prev_row, prev_column) not in visited)):
		counter += next_character(copy.deepcopy(visited), prev_row, prev_column, dictionary)
	# Adds the charcter W of the current pos
	if(prev_column >= 0 and ((current_row, prev_column) not in visited)):
		counter += next_character(copy.deepcopy(visited), current_row, prev_column, dictionary)
	# Adds the charcter SW of the current pos
	if(prev_column >= 0 and len(board[current_row]) > next_row and ((next_row, prev_column) not in visited)):
		counter += next_character(copy.deepcopy(visited), next_row, prev_column, dictionary)
	return counter
def create_board(input):
	arr = [[input[0], input[1], input[2], input[3]],
	[input[4], input[5], input[6], input[7]],
	[input[8], input[9], input[10], input[11]],
	[input[12], input[13], input[14], input[15]]]
	print(input[0], input[1], input[2], input[3])
	print(input[4], input[5], input[6], input[7])
	print(input[8], input[9], input[10], input[11])
	print(input[12], input[13], input[14], input[15])
	return arr


pym = PyMouse()

pym.click(445, 1240, button=1, n=1)
time.sleep(1.2)
screen = Gdk.get_default_root_window().get_screen()
w = screen.get_active_window()
pb = Gdk.pixbuf_get_from_window(w, *w.get_geometry())
im = Image.frombytes('RGB', (pb.props.width, pb.props.height), pb.get_pixels(), "raw", 'RGB', pb.props.rowstride)
im.save('testcrop3.png','png')

#im = Image.open('testcrop.png')
im = im.convert('L')
enhancer = ImageEnhance.Brightness(im)
im = enhancer.enhance(10)
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(10)
#im.show()
im.save('testcrop3.png','png')
count=0
for i in range(0, 4, 1):
    for j in range(0, 4, 1):
        count += 1
        imCrop = im.crop((100+142*j,506+142*i,142+142*j,548+142*i))
        imCrop.save('./important/character_'+str(count)+'.png')

quad1 = Image.new('L',(42*4,42),'white')
for i in range(0, 4, 1):
    imPaste = Image.open('./important/character_'+str(i+1)+'.png')
    quad1.paste(imPaste, (0+i*42,0,42+i*42,42))
#quad1.show()

quad2 = Image.new('L',(42*4,42),'white')
for i in range(0, 4, 1):
    imPaste = Image.open('./important/character_'+str(i+5)+'.png')
    quad2.paste(imPaste, (0+i*42,0,42+i*42,42))
#quad2.show()

quad3 = Image.new('L',(42*4,42),'white')
for i in range(0, 4, 1):
    imPaste = Image.open('./important/character_'+str(i+9)+'.png')
    quad3.paste(imPaste, (0+i*42,0,42+i*42,42))
#quad3.show()

quad4 = Image.new('L',(42*4,42),'white')
for i in range(0, 4, 1):
    imPaste = Image.open('./important/character_'+str(i+13)+'.png')
    quad4.paste(imPaste, (0+i*42,0,42+i*42,42))
#quad4.show()

finalcomp = Image.new('L',(42*4,42*4+90),'white')
finalcomp.paste(quad1,(0,0,42*4,42))
finalcomp.paste(quad2,(0,0+72,42*4,42+72))
finalcomp.paste(quad3,(0,0+72*2,42*4,42+72*2))
finalcomp.paste(quad4,(0,0+72*3,42*4,42+72*3))
finalcomp.save('./important/finalcom.png','png')
finalcomp.save('testcrop3.png','png')
finalcomp.show()

text = pytesseract.image_to_string(finalcomp)
print(text)

finalstr = ''
for i in range(len(text)):
    print(text[i])
    if text[i]=='|':
        finalstr += 'I'
        continue
    if text[i]=='!':
        finalstr += 'I'
        continue
    if text[i]=='1':
        finalstr += 'I'
        continue
    if text[i]==' ':
        continue
    if text[i]=='\n':
        continue
    finalstr += text[i]
finalstr = finalstr.lower()
print(finalstr)


f = open('wordlist.txt', 'r')
dictionary = set(f.read().splitlines())

check = 'k'
#check = input('is that ok?')
input = check
if check == 'k':
	input = finalstr

board = create_board(input)
word_candidates = []
iterator = []
for row in range(0, 4):
	for column in range(0, 4):
		iterator.append(([], row, column, dictionary))
results = []
tstart = time.time()
with Pool(1) as pool:
	results = pool.starmap(next_character, iterator)
#word_candidates.sort(key=len, reverse=True)
#print(sum(results))
#pprint(word_candidates)
