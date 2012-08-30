'''
Program to simulate the rotating magnetic field in a 3 phase motor
The following are the color codes used:

Red     - R phase
Yellow  - Y phase
Blue    - B phase
Grey    - Temporary vectors to help calculate the resultants
Dark Grey-Vector resultant of two vectors
Green   - Final resultant

Note: The output will be a sequence of 490 images. To create an image
      (linux only), use the following command in the same folder:
      $ ffmpeg -f image2 -i im%d.bmp -vcodec mpeg4 -b 1200k output.avi

        The output file is output.avi
'''
__author__ = 'Vishwanath'
__version__ = '0.1'

import Image
import ImageDraw
import os

from math import sin,cos,atan2,pi

try:
        os.mkdir('output')
except:
        pass
path = []
def resDraw(draw, centre, vec1, vec2, vec3):
        global path
        xc,yc = centre
        x1,y1 = vec1
        x2,y2 = vec2
        x3,y3 = vec3

        theta1 = atan2(y1-yc,x1-xc)
        
        r1 = (xc-x1)*(xc-x1) + (yc-y1)*(yc-y1)
        r1 = pow(r1,0.5)
        
        xres1 = x2 + r1*cos(theta1)
        yres1 = y2 + r1*sin(theta1)

        draw.line((x1,y1,xres1,yres1),fill = (200,200,200))
        draw.line((x2,y2,xres1,yres1),fill = (200,200,200))
        draw.line((xc,yc,xres1,yres1),fill = (100,100,100))

        theta2 = atan2(yres1-yc,xres1-xc)

        r2 = (xc-xres1)*(xc-xres1) + (yc-yres1)*(yc-yres1)
        r2 = pow(r2,0.5)

        xres2 = x3 + r2*cos(theta2)
        yres2 = y3 + r2*sin(theta2)

        draw.line((x3,y3,xres2,yres2),fill = (200,200,200))
        draw.line((xres1,yres1,xres2,yres2),fill = (200,200,200))
        draw.line((xc,yc,xres2,yres2),fill = (0,255,0),width = 2)

        path.append((int(xres2),int(yres2)))

im = Image.new('RGB',(400,400),(255,255,255))
canvas = ImageDraw.Draw(im)

TIME=480
w = 2*pi/TIME
A=100

for t in range(TIME+10):
        im = Image.new('RGB',(800,800),(255,255,255))
        xc,yc = im.size
        xc = xc//2
        yc = yc//2
        
        R = A*sin(w*t)
        Y = A*sin(w*t + (2*pi)/3)
        B = A*sin(w*t + (4*pi)/3)
        
        Rx = xc + R*cos(0)
        Ry = yc + R*sin(0)
        
        Yx = xc + Y*cos((2*pi)/3)
        Yy = yc + Y*sin((2*pi)/3)

        Bx = xc + B*cos((4*pi)/3)
        By = yc + B*sin((4*pi)/3)

        draw = ImageDraw.Draw(im)
        
        draw.line((xc,yc,int(Rx),int(Ry)),fill = (255,0,0),width = 2)
        draw.line((xc,yc,int(Yx),int(Yy)),fill = (255,255,0),width = 2)
        draw.line((xc,yc,int(Bx),int(By)),fill = (0,0,255),width = 2)
        resDraw(draw, (xc,yc), (Rx,Ry), (Yx,Yy), (Bx,By))
        for i in path:
                im.putpixel(i,(0,0,100))
        im.save('output/im'+str(t)+'.bmp')
