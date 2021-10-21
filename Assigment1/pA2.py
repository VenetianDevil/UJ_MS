#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

N = 5000
X = []
Y = []
density = []
x0 = y0 = .3
gamma = .5

def f(y):
    return (1/(math.pi*gamma*(1+((y-y0)/gamma)**2)))

# odwrotnosc dystrybuanty
def F(x):
    return gamma*math.tan((math.pi/2)*(2*x - 1))+x0

def warSum(N, result, u):
    value = 0
    for i in range(1, N):
        value += (result[i]-u)**2
    return value

X = np.random.normal(y0, gamma, N)
X = np.sort_complex(X)

for x in X:
    Y.append(F(x))

for x in X:
    density.append(f(x))

plt.text(4, 0.6, r'$y_0$ = {}'.format(y0))
plt.text(4, 0.55, '\u03B3 = {}'.format(gamma))
plt.hist(Y, range=[-5, 5], density=True, bins=20)
plt.plot(X, density)
plt.show()

avg = sum(Y)/N
wariancja = 1/N * warSum(N, Y, avg)
print("avg = ", avg)
print("wariancja = ", wariancja)