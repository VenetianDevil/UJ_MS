#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

u=0
s2=1
N = 5000
X = []
Y = []
density = []
x0 = y0 = 0
gamma = 1

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

while len(X) < N:
    X.append(random.uniform(0, 1))

X = np.sort_complex(X)

for x in X:
    Y.append(F(x))

for y in Y:
    density.append(f(y))

plt.hist(X, normed=True, bins=20)
# plt.plot(result, density)
plt.show()

# avg = sum(result)/N
# wariancja = 1/N * warSum(N, result, u)
# # avg = math.avg(result)
# print("avg = ", avg)
# print("wariancja = ", wariancja)