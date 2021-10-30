import gi
import time
import pytesseract
gi.require_version('Gtk', '3.0')
from gi.repository import Gdk
from pymouse import PyMouse
from PIL import Image, ImageEnhance
import textract



'''
pym = PyMouse()
pym.click(445, 1240, button=1, n=1)
time.sleep(1.2)
screen = Gdk.get_default_root_window().get_screen()
w = screen.get_active_window()
pb = Gdk.pixbuf_get_from_window(w, *w.get_geometry())
im = Image.frombytes('RGB', (pb.props.width, pb.props.height), pb.get_pixels(), "raw", 'RGB', pb.props.rowstride)
im.save('testcrop2.png','png')
'''

im = Image.open('testcrop.png')
im = im.convert('L')
enhancer = ImageEnhance.Brightness(im)
im = enhancer.enhance(10)
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(10)
#im.show()

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
finalcomp.show()

text = pytesseract.image_to_string(finalcomp)
print(text)

finalstr = ''
for i in range(len(text)):
    print(text[i])
    if text[i]=='|':
        finalstr += 'I'
        continue
    if text[i]==' ':
        continue
    if text[i]=='\n':
        continue
    finalstr += text[i]
finalstr = finalstr.lower()
print(finalstr)
