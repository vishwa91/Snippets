#/bin/bash

from scipy import *
from matplotlib.pyplot import *

u0 = 1
a = 0.125
b = 0.15
k = 0.75
B = 1
C = 1
T = 1

for T in arange(0.1,2,0.1):
    xe = pow((a/b)*pow(C, B), (1.0/B-k+2))

    A1 = (k-2)*a*pow(T, k-2) * pow(xe, k-1)
    B1 = -B*b*pow(T,B)*pow(xe, B+1)/pow(C,B)

    freq = arange(-100, +100, 0.001)
    L = 1/(1j*freq - A1 - B1*exp(-1j*freq*T))
    line = 'T = '+str(T)
    #plot(real(L), imag(L), label = line)
    plot(freq, angle(L))

legend(loc = 'lower right')
show()
