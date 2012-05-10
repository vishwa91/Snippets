'''
	Author:  		Vishwanath <vishwa.hyd@gmail.com>
	Version:		1.0
	Dependencies:	Python Image Library
	
	This module converts an image to its ASCII equivalent.
	Presently, there are only 4 characters being used.
'''

import Image
import time

def check_pixel(x,y,rows,cols):
    if (x > rows-1) or (y > cols-1) or (x < 0) or (y < 0):
        return 0
    else:
        return 1


def namer_pic(fname):
    name = ''
    for i in fname:
        if i == '.':
            break
        else:
            name += i
    name = name + '_text_pic.txt'
    return name



info = open('info.txt')
pic_in = info.readline()
pic = ''
for i in pic_in:
    if i == '\n':
        break
    else:
        pic = pic + i

print 'Loading '+pic+' image'
print "Please note,if the picture's resolution is too high,the program will take a lot of time"


im = Image.open(pic)
name = namer_pic(pic)

f = file(name,'wt')

rows = im.size[0]
cols = im.size[1]
res = (rows+cols)/120

im = im.convert('L')

im = im.resize((rows/res,cols/res))

rows = im.size[0]
cols = im.size[1]

print 'Writing to file'

for i in range(cols):
    for j in range(rows):
        if im.getpixel((j,i)) <50:
            f.write('@')
        elif im.getpixel((j,i)) <100:
            f.write('o')
        elif im.getpixel((j,i)) <150:
            f.write('*')
        elif im.getpixel((j,i)) <200:
            f.write('.')
        else:
            f.write(' ')
    f.write('\n')

signature = 'Program created by Vishwanath'

for i in signature:
    f.write(i)

f.close()

print 'File generated.Please look for '+name+'file for the text image'
print 'Thank you for using my program'
print 'The program will close automatically.please dont interrupt'
print 'Picturizer created by Vishwanath'
#time.sleep(2)
