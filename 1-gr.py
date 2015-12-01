import numpy as np
import matplotlib.pyplot as plt
import math


N=1
x = int(input())
ya = math.log(2.7**(1/(1 + np.sin(x)/(1.25 + 1/x**15))), 1 + x*x)
x = int(input())
yb = math.log(2.7**(1/(1 + np.sin(x)/(1.25 + 1/x**15))), 1 + x*x)
x = int(input())
yc = math.log(2.7**(1/(1 + np.sin(x)/(1.25 + 1/x**15))), 1 + x*x)
print(ya, yb, yc)


N=2
x=np.arange(-10,10.01,0.01)
plt.plot(x, x*x - 6 - x)
plt.show()
x1 = (1 - (1 + 6*4)**0.5) / 2
x2 = (1 + (1 + 6*4)**0.5) / 2
print (x1, x2)


N=3
x=np.arange(-10,10.01,0.01)
plt.plot(x, math.log((x**2 + 1) * math.exp(- (x*x)**0.5 / 10)), 1 + np.tan (1 / (1 + np.sin(x))))
plt.show()


N=4
import pylab
from matplotlib import mlab



tmin = -20.0
tmax = 20.0
dt = 0.01
tlist = mlab.frange (xmin, xmax, dx)
a = 0

pylab.ion()
for n in range (50):
        xlist = [math.sin (t + a) for t in tlist]
        ylist = [2 * math.cos (t) for t in tlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()
        a += 1

pylab.close()


N=5
x=np.arange(-10,10.01,0.01)
plt.plot(x, eval (input()))

