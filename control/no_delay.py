#/bin/python

from scipy import *
from matplotlib.pyplot import *

x0 = 1
a = 0.125
b = 0.15
k = 0.75
B = 1
C = 1
T = 1

niters = 50
numerical_iters = 10
xval = zeros(niters)

for T in arange(0.1, 1, 0.05):
    xval[0] = x0
    for i in range(1, niters):
        x_old = 0.1
        x_new = 0.1
        for j in range(numerical_iters):
            x_new = xval[i-1] + (a*pow(T, k-2)*pow(x_old,k)
                                 - b*pow(T, B-1)*pow(x_old, B+2)/pow(C, B))
            x_old = x_new
        xval[i] = x_new
    l = 'T = ' + str(T)
    myplot = plot(range(niters), xval, label = l)
    #phase_plot = plot(xval[:-1], xval[:-1]-xval[1:], label = l)
legend(loc='upper right')
show()
