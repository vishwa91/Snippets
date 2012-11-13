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

niters = 500
for k in arange(0.1,1,0.1):
    xe = pow((a/b)*pow(C, B), (1.0/B-k+2))
    numer = B*b*pow(T,B)*pow(xe, B+1)/pow(C,B)
    denom = (k-2)*a*pow(T,k-2)*pow(xe, k-1)

    t = arange(0,500, 1)
    u = pow((1-numer)/(1-denom), t-1)*u0
    plot(t, u)
show()
