#/bin/python

from scipy import *
from matplotlib.pyplot import *

x0 = 1
a = 0.125
b = 0.5
k = 0.75
B = 1
C = 1
T = 1
p0 = 0
r = 0.8
niters = 50
numerical_iters = 10
xval = zeros(niters)
pval = zeros(niters)

for T in range(1, 10):
    xval[0] = x0
    pval[0] = p0
    for i in range(T, niters):
        x_old = 1
        x_new = 1
        p_old = 1
        p_new = 1
        for j in range(numerical_iters):
            p_new = (sum(pow(xval[:i]/C, B)) - sum(pval[:i]))/r
            x_new = xval[i-1] + (1.0/T) * xval[i-T]*(a * pow(T*x_old, k-1) -
                                        b*T*x_old*p_new)
            x_old = x_new
            p_old = p_new
        xval[i] = x_new
        pval[i] = p_new
    l = 'T = ' + str(T)
    myplot = plot(range(niters), xval, label = l)
    #phase_plot = plot(xval[:-1], xval[:-1]-xval[1:], label = l)
legend(loc='upper right')
show()
