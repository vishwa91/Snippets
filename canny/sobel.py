import numpy
import scipy
from scipy import ndimage

def sobelFunction(s):
    im = scipy.misc.imread(s)
    im = im.astype('int32')
    imagename = s[:-4]
    dx = ndimage.sobel(im, 0)  # horizontal derivative
    dy = ndimage.sobel(im, 1)  # vertical derivative
    mag = numpy.hypot(dx, dy)  # magnitude
    mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
    scipy.misc.imsave(imagename+'SobelOutput.jpg', mag)
