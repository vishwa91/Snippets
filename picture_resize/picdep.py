'''
    Picture depricator.
    This program will help create a smaller image without destroying the
    pixel aspect ratio. The resized image need not completely comply with the
    original image.

    The script is to be used as a command line program. See the following
    example:
    <prompt>picdep example.jpg 917x427 SYM

    The output is example.jpg
    The first arguement is the image, the second is the final image resolution
    and the final arguement is the snap window arguement. The following are
    the snap window arguements:

    SYM - symmetric subset of the input image
    END - Lower subset/ right subset of input image
    STR - Upper subset/ left subset of input image

    contact: Vishwanath,
             email: vishwa.hyd@gmail.com
             phone: 9444357552
'''

__author__ = 'Vishwanath'
__version__ = '0.1'

from scipy import *
from scipy.ndimage import *
import Image
import sys
from time import sleep

argc = len(sys.argv)

if argc != 4:
    print 'Usage: picdep input.jpg heightxwidth SYM/END/STR'
    print 'image should be jpg or bmp only'
    print 'last arguement should be SYM or END or STR'
    sleep(2)
    sys.exit('Inavalid arguement count')

try:
    t = sys.argv[2].index('x')
    WIDTH = int(sys.argv[2][:t])
    HEIGHT = int(sys.argv[2][t+1:])
except:
    sys.exit('Invalid resolution field')

try:
    imname = sys.argv[1]
    print 'Loading image'
    imin = imread(imname)
except:
    sys.exit('Invalid image name')

try:
    symarg = sys.argv[3]
except:
    sys.exit('Arguement '+sys.argv[3]+' not supported')

print 'Extracting layers'
imr = imin[:,:,0]
img = imin[:,:,1]
imb = imin[:,:,2]

x,y = imr.shape
xratio = (HEIGHT*1.0)/x
yratio = (WIDTH*1.0)/y
scale = max(xratio,yratio)
print 'Scaling down image at ',scale
imrnew = zoom(imr,scale)
imgnew = zoom(img,scale)
imbnew = zoom(imb,scale)

if scale == xratio:
    t = (imrnew.shape[1] - WIDTH)//2
    if symarg == 'SYM':
        imrout = imrnew[:,t:-t]
        imgout = imgnew[:,t:-t]
        imbout = imbnew[:,t:-t]
    elif symarg == 'STR':
        imrout = imrnew[:,:-2*t]
        imgout = imgnew[:,:-2*t]
        imbout = imbnew[:,:-2*t]
    else:
        imrout = imrnew[:,2*t:]
        imgout = imgnew[:,2*t:]
        imbout = imbnew[:,2*t:]
        
else:
    t = (imrnew.shape[0]-HEIGHT)//2
    if symarg == 'SYM':
        imrout = imrnew[t:-t,:]
        imgout = imgnew[t:-t,:]
        imbout = imbnew[t:-t,:]
    elif symarg == 'STR':
        imrout = imrnew[:-2*t,:]
        imgout = imgnew[:-2*t,:]
        imbout = imbnew[:-2*t,:]
    else:
        imrout = imrnew[2*t:,:]
        imgout = imgnew[2*t:,:]
        imbout = imbnew[2*t:,:]

x,y = imrout.shape
imout = zeros((x,y,3))
imout[:,:,0]=imrout
imout[:,:,1]=imgout
imout[:,:,2]=imbout
imout = imout.astype(uint8)
im = Image.fromarray(imout)
t = 0
while True:
    try:
        t = imname.index('/')
        imname[t] = '^'
    except ValueError:
        i = imname.index('.')
        im.save('out.jpg')
        print imname
        print i,t
        t = 'Saved'
        break
if t != 'Saved':
    im.save(imname)
