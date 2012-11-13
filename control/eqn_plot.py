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

niters = 500
numerical_iters = 10
xval = zeros(niters)
#xval[:T] = 1

for b in arange(1.0, 1.1, 0.01):
    xval[0] = x0
    for i in range(T, niters):
        x_old = 1
        x_new = 1
        for j in range(numerical_iters):
            x_new = xval[i-1] + (1.0/T) * xval[i-T]*(a * pow(T*x_old, k-1) -
                                        b * T * x_old*pow(T*xval[i-T]/C, B))
        xval[i] = x_new
    l = 'b = ' + str(b)
    myplot = plot(range(niters), xval, label = l)
    #phase_plot = plot(xval[:-1], xval[:-1]-xval[1:], label = l)
legend(loc='upper right')
show()
